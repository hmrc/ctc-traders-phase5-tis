import pprint

from data_types import MessageField, MessageCategory, Rule
from parser import find_pages, read_and_transform, extract_rules
from PyPDF2 import PdfReader
import sys
from os.path import abspath, expanduser
from deepdiff import DeepDiff
from typing import Optional

expected_message_types = [
    "IE004",
    "IE007",
    "IE009",
    "IE013",
    "IE014",
    "IE015",
    "IE019",
    "IE022",
    "IE025",
    "IE028",
    "IE029",
    "IE035",
    "IE043",
    "IE044",
    "IE045",
    "IE051",
    "IE055",
    "IE056",
    "IE057",
    "IE060",
    "IE170",
    "IE182",
    "IE928"
]

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


result: list[str] = []

# To support the diffing engine and to remove order (it matters less for the TIS), we'll turn the list of categories
# into dict trees.
result.append("--------------------------------")
result.append("--- MESSAGE TYPE DIFFERENCES ---")
result.append("--------------------------------")

for message_type in expected_message_types:
    result.append(f"Diff for {message_type}")
    old_tree = old[0][message_type]
    new_tree = new[0][message_type]
    result.append(pprint.pformat(DeepDiff(create_tree(old_tree), create_tree(new_tree), ignore_order=True)))
    result.append("------")

result.append("--------------------------------")
result.append("------- RULE DIFFERENCES -------")
result.append("--------------------------------")

old_rules = flatten_rules(old[1])
new_rules = flatten_rules(new[1])
diff = DeepDiff(old_rules, new_rules, ignore_order=True)

if diff.keys().__contains__("dictionary_item_added"):
    added_rules = list(sorted(map(lambda x: x.replace("root['", "").replace("']", ""), diff['dictionary_item_added'])))
    result.append(f"Rules added: {added_rules}")
    result.append("-- --")
    for rule_code in added_rules:
        result.append(f"""Rule {rule_code} - Technical:
        
        New rule:
        {new_rules[rule_code][0]}
        
        ------
        
        Rule {rule_code} - Functional:
        
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
    result.append(f"""Rules changed: {changed_rules[0]} - {changed_rules[1]}""")
    result.append("-- --")
    result.append("-- Rule diffs --")
    for rule_code, rule_type in changed_rules:
        if rule_type == "Technical":
            index = 0
        else:
            index = 1
        result.append(f"""Rule {rule_code} - {rule_type}:
        
        Old rule:
        {old_rules[rule_code][index]}
        
        New rule:
        {new_rules[rule_code][index]}
        ------""".replace("        ", ""))

result.append("--------------------------------")
result.append("------------- END --------------")
result.append("--------------------------------")

with open("diff_result.txt", "w") as file:
    for line in result:
        file.write(f"{line}\n")

print("Diff calculated and saved to 'diff_result.txt'")
