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
from PyPDF2 import PdfReader
from parser import find_pages, read_and_transform, extract_rules
import render
import sys
from os.path import abspath, expanduser

if len(sys.argv) > 1:
    pdf_file_name = abspath(expanduser(sys.argv[1]))
else:
    pdf_file_name = abspath("ddnta.pdf")

print(f"Reading PDF from {pdf_file_name}")
pdf_reader = PdfReader(pdf_file_name)

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

# There are also T rules, but we don't publish them
expected_rules = ["B", "C", "E", "G", "R", "S"]

# get pages
entries, rules_start_page = find_pages(pdf_reader, expected_message_types)

for e in entries:
    render.write_message_type_file(e[0], read_and_transform(pdf_reader, e[1], e[2], e[0]))

extracted_rules = extract_rules(pdf_reader, rules_start_page)

for cat, ruleset in extracted_rules.items():
    if expected_rules.__contains__(cat):
        render.write_rules_file(cat, ruleset)

