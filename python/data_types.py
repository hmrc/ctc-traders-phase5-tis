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
import re


class MessageField:

    regex = "(CL\\d{3})?([BCEGRS]\\d{4})?$"

    def __init__(self):
        self.field: str = ""
        self.required: str = ""
        self.format: str = ""
        self.code_list: str = ""
        self.rules: list[str] = list()

    def parse_line(self, line: str):
        # Reference number Ran8CL172R0901 (Everything)
        # Binding itinerary Rn1CL027 (no rule)
        # Release date Ran10 G0002 (no code list)
        # Message recipient Ran..35 (no rule, no codelist)

        #Sequence number Rn..5 R0987

        # We'll start from the right, a rule is always 5 characters, a letter and four numbers. Do we have that?
        match = re.search(self.regex, line.strip())
        captured = match.group(0)
        field_tup = line.removesuffix(captured).strip().rpartition(" ")
        self.field = field_tup[0].strip()
        # we then parse the line as 1xD[potential rule]
        self.required = field_tup[2][0].strip()
        self.format = field_tup[2][1:].strip()
        self.code_list = match.group(1)
        if match.group(2) is not None:
            self.rules.append(match.group(2))

    def add_rule(self, line: str):
        self.rules.append(line)

    def __str__(self):
        return f"""
         Field: {self.field}
         Required: {self.required}
         Format: {self.format}
         Code List: {self.code_list}
         Rules: {self.rules}
         """


class MessageCategory:

    hyphen_pattern = re.compile("^(-+)")

    def __init__(self, message_type: str):
        self.message_type: str = message_type
        self.category: str = ""
        self.category_name_only: str = ""
        self.multiplicity: str = ""
        self.required: str = ""
        self.rules: list[str] = list()
        self.children: list[MessageField] = list()
        self.level = 0

    def parse_line(self, line: str):
        # "------TRANSPORT CHARGES 1xDC0186"
        category_tup = line.rpartition(" ")
        self.category = re.sub(self.hyphen_pattern, lambda x: f"{x.group(0)} ", category_tup[0])
        self.category_name_only = category_tup[0].strip().replace("-", "")
        self.level = int(category_tup[0].count("-") / 3)
        # we then parse the line as 1xD[potential rule]
        metadata_tup = category_tup[2].partition("x")
        self.multiplicity = f"{metadata_tup[0]}x"
        try:
            self.required = metadata_tup[2][0]
        except Exception as e:
            print(metadata_tup)
            raise e
        if len(metadata_tup[2]) > 1:
            self.rules.append(metadata_tup[2][1:])

    def add_rule(self, line: str):
        self.rules.append(line)

    def add_field(self, field: MessageField):
        self.children.append(field)

    def __str__(self):
        children: list[str] = list()
        for c in self.children:
            children.append(c.__str__())
        return f"""
                Category: {self.category}
                Multiplicity: {self.multiplicity}
                Required: {self.required}
                Rules: {self.rules}
                Children: {children}
                """

    def simple_str(self):
        children: list[str] = list()
        for c in self.children:
            children.append(c.field.__str__())
        return "\n".join([self.category, *children])


class Rule:

    def __init__(self, rule_text: list[str]):
        # first line will be [A-Z]\d{4}\s+Technical Description
        first_line = rule_text[0]
        self.rule_category = first_line[0]
        self.rule_code = first_line[0:5]

        # we split the list on "Functional Description:"
        idx = rule_text.index("Functional Description:")
        self.technical_description = "\n".join(rule_text[1:idx])
        self.functional_description = "\n".join(rule_text[idx+1:len(rule_text)])
