#!/usr/bin/python3
"""
 Copyright 2023 HM Revenue & Customs

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""
import pprint

from data_types import MessageField, MessageCategory, Rule
from parser import find_pages, read_and_transform, extract_rules
from PyPDF2 import PdfReader
import sys
from os.path import abspath, expanduser
from message_reference import expected_message_types
from deepdiff import DeepDiff
from typing import Optional

expected_message_types = expected_message_types()

if len(sys.argv) != 3:
    print("Expected two arguments -- 'python ./diff.py <old file> <new file>'")
    exit(-1)

old_pdf = abspath(expanduser(sys.argv[1]))
new_pdf = abspath(expanduser(sys.argv[2]))


def get_data_from_pdf(filename: str) -> tuple[dict[str, list[MessageCategory]], dict[str, list[Rule]]]:
    pdf_reader = PdfReader(filename)
    entries, rules_start_page = find_pages(pdf_reader, expected_message_types)

    message_type_data: dict[str, list[MessageCategory]] = {}
    for e in entries:
        print(e)
        message_type_data[e[0]] = read_and_transform(pdf_reader, e[1], e[2], e[0])

    extracted_rules = extract_rules(pdf_reader, rules_start_page)
    return message_type_data, extracted_rules


print(f"Parsing OLD data {old_pdf}")
old = get_data_from_pdf(old_pdf)
print("------")
print(f"Parsing NEW data {new_pdf}")
new = get_data_from_pdf(new_pdf)
print("------")


class TreeNode:

    @classmethod
    def of_category(cls, mc: MessageCategory):
        children = mc.children
        # avoids ordering issues, we just care about the fact they are there, and as we'll put the children into the
        # map, we don't need this here anyway.
        mc.children = []
        return cls(mc, None, dict(list(map(lambda c: (c.field, cls.of_field(c)), children))))

    @classmethod
    def of_field(cls, mf: MessageField):
        return cls(None, mf, None)

    def __init__(self, mc: Optional[MessageCategory], mf: Optional[MessageField], node):
        self.category = mc
        self.field = mf
        self.node: dict[str, TreeNode] = node

    def add_child(self, mc: MessageCategory):
        if self.category is None:
            error = f"{mc.category_name_only} (level {mc.level}) can't be a child of a field"
            raise RuntimeError(error)
        elif self.category.level != mc.level - 1:
            error = f"{mc.category_name_only} (level {mc.level}) can't be a child of {self.category.category_name_only} (level {self.category.level}"
            raise RuntimeError(error)
        else:
            node = self.of_category(mc)
            self.node[mc.category_name_only] = node
            return node


def create_tree(l: list[MessageCategory]):
    root: Optional[TreeNode] = None
    stack: list[TreeNode] = []
    for i in l:
        if len(stack) > 0:
            stack = stack[0:i.level]
            node = stack[-1].add_child(i)
            stack.append(node)
        else:
            root = TreeNode.of_category(i)
            stack.append(root)

    return root


def flatten_rules(r: dict[str, list[Rule]]):
    flattened_rules: dict[str, tuple[str, str]] = {}
    for rules in r.values():
        for r in rules:
            flattened_rules[r.rule_code] = (r.technical_description, r.functional_description)

    return flattened_rules


def create_rule_tuple(rule: str):
    rule_code = rule.replace("root['", "").replace("']", "").replace("[0]", "").replace("[1]", "")
    if rule.__contains__("[0]"):
        rule_type = "Technical"
    else:
        rule_type = "Functional"
    return rule_code, rule_type


result: list[str] = ["--------------------------------",
                     "--- MESSAGE TYPE DIFFERENCES ---",
                     "--------------------------------"]

# To support the diffing engine and to remove order (it matters less for the TIS), we'll turn the list of categories
# into dict trees.

for message_type in expected_message_types:
    print(f"Generating diff for message type {message_type}")
    result.append(f"Diff for {message_type}")
    old_tree = old[0][message_type]
    new_tree = new[0][message_type]
    result.append(pprint.pformat(DeepDiff(create_tree(old_tree), create_tree(new_tree), ignore_order=True)))
    result.append("------")

result.append("--------------------------------")
result.append("------- RULE DIFFERENCES -------")
result.append("--------------------------------")

print(f"Generating diff for message rules...")

old_rules = flatten_rules(old[1])
new_rules = flatten_rules(new[1])
diff = DeepDiff(old_rules, new_rules, ignore_order=True)

rules_to_print: list[str] = [
    "-- --",
    "-- Rule diffs --"
]

if diff.keys().__contains__("dictionary_item_added"):
    added_rules = list(sorted(map(lambda x: x.replace("root['", "").replace("']", ""), diff['dictionary_item_added'])))
    result.append(f"Rules added: {added_rules}")
    for rule_code in added_rules:
        rules_to_print.append(f"""Added rule {rule_code} - Technical:
        
        New rule:
        {new_rules[rule_code][0]}
        
        ------
        
        Added rule {rule_code} - Functional:
        
        New rule:
        {new_rules[rule_code][1]}
        
        ------
        """.replace("        ", ""))

if diff.keys().__contains__("dictionary_item_removed"):
    removed_rules = list(
        sorted(map(lambda x: x.replace("root['", "").replace("']", ""), diff['dictionary_item_removed'])))
    result.append(f"Rules removed: {removed_rules}")

if diff.keys().__contains__("values_changed"):
    changed_rules = list(sorted(map(create_rule_tuple, diff['values_changed']), key=lambda x: x[0]))
    fmt_change_rules = f"Rules changed: {list(dict.fromkeys(map(lambda x: x[0], changed_rules)))}"
    result.append(fmt_change_rules)
    for rule_code, rule_type in changed_rules:
        if rule_type == "Technical":
            index = 0
        else:
            index = 1
        rules_to_print.append(f"""Rule {rule_code} - {rule_type}:
        
        Old rule:
        {old_rules[rule_code][index]}
        
        New rule:
        {new_rules[rule_code][index]}
        ------""".replace("        ", ""))

if len(rules_to_print) > 2:
    for r in rules_to_print:
        result.append(r)

result.append("--------------------------------")
result.append("------------- END --------------")
result.append("--------------------------------")

with open("diff_result.txt", "w") as file:
    for line in result:
        file.write(f"{line}\n")

print("Diff calculated and saved to 'diff_result.txt'")
