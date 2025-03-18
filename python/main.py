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

----

This script takes the DDNTA Q2 PDF and turns it into a series of markdown files for rendering on the HMRC CTC Phase 5 TIS

Read the included README.md file to understand usage of this script.
"""
import pprint

from PyPDF2 import PdfReader

import code_lists
from parser import find_pages, read_and_transform, extract_rules
from data_types import MessageCategory, MessageField, Rule
from message_reference import expected_message_types
import render
import sys
import re
from os.path import abspath, expanduser

if len(sys.argv) > 1:
    pdf_file_name = abspath(expanduser(sys.argv[1]))
else:
    pdf_file_name = abspath("ddnta.pdf")

print(f"Reading PDF from {pdf_file_name}")
pdf_reader = PdfReader(pdf_file_name)

expected_message_types = expected_message_types()

# There are also T rules, but we don't publish them
expected_rules = ["B", "C", "E", "G", "R", "S"]

# get pages
entries, rules_start_page = find_pages(pdf_reader, expected_message_types)

transformed_entries: dict[str, list[MessageCategory]] = dict()

rule_set: set[str] = set()
for e in entries:
    # Here, we're getting the rules associated with data groups and items
    # such that we don't write those that are common domain only
    list_groups = read_and_transform(pdf_reader, e[1], e[2], e[0])
    for cat in list_groups:
        for rule in cat.rules:
            rule_set.add(rule)

        for item in cat.children:
            for rule in item.rules:
                rule_set.add(rule)

    transformed_entries[e[0]] = list_groups

for message_type, list_of_groups in transformed_entries.items():
    render.write_message_type_file(message_type, list_of_groups)

extracted_rules = extract_rules(pdf_reader, rules_start_page)

# for each rule set, if the rule is not in the external domain messages
# we will drop them from rendering.
for key, rule_list in extracted_rules.items():
    extracted_rules[key] = [rule for rule in rule_list if rule.rule_code in rule_set]

for cat, ruleset in extracted_rules.items():
    if expected_rules.__contains__(cat):
        render.write_rules_file(cat, ruleset)

# finally, a diagnostic -- in each rule we check for CL\d{3} and compare it against our code lists. If it isn't available
# from Europa, we'll print it out here.
missing_cls: dict[str, list[str]] = {}

# lists that have a Europa download
available_lists = [cl.code_list for cl in code_lists.load_code_list().values()]

cl_regex = re.compile("CL\\d{3}")

for rule_list in extracted_rules.values():
    for rule in rule_list:
        # find the CLs
        found = cl_regex.findall(rule.technical_description)
        found += cl_regex.findall(rule.functional_description)

        # deduplicate
        found_set = set(found)

print("Generation complete")
