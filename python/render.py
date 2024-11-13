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
import os
import re
from inspect import cleandoc
from os import path
from typing import Optional

from code_lists import replace_code_list, replace_code_list_full_string
from data_types import MessageCategory, MessageField, Rule

save_location = path.join("..", "source", "documentation", "partials")

special_formats = {
    "Message sender": """an..35""",
    "Message recipient": """an..35"""
}

head_tag = """<table cellspacing="0">"""
header_row = """
<tr>
<th>
   Field Name
  </th>
<th>
   Priority
  </th>
<th>
   Format / Max Repeat
  </th>
<th>
   Code Lists
  </th>
<th>
   Rules
  </th>
</tr>
"""

tail = "</table>"


def linkify_rule(rule: str) -> str:
    return f"""<a href="rules-{rule.lower()[0]}.html#{rule.lower()}">{rule}</a>"""


def create_rules(rules: list[str]):
    if len(rules) > 0:
        return "<br />".join(map(linkify_rule, rules))
    else:
        return "&nbsp;"


def render_optional_code_list(value: Optional[str]) -> str:
    """
    Creates links for code lists that have associated URIs

    :param value: The codelist, if there is one
    :return: A non-breaking space if no code list, or the codelist, potentially with a link
    """
    if value is None:
        return "&nbsp;"
    else:
        return replace_code_list(value)

# ---- Rendering for Message Types

def render_category_row(category: MessageCategory) -> str:
    """
    Creates a table row for a category and associated rows for the fields

    :param category: The category
    :return: The HTML
    """
    # We convert --- from the DDNTA to -.
    cat = category.category.replace("---", "-&nbsp;")
    # Fields will gain hyphens for easier visualisation of hierarchy
    hyphens = cat.count("-")
    c = cleandoc(f"""
    <tr>
        <td><strong>{cat}</strong></td>
        <td>{category.required}</td>
        <td>{category.multiplicity}</td>
        <td>&nbsp;</td>
        <td>{create_rules(category.rules)}</td>
    </tr>""")
    # Render the fields and return the category and fields together
    return c + render_children_fields(category.children, hyphens + 1)


def render_children_fields(fields: list[MessageField], hyphens: int) -> str:
    """
    Renders fields

    :param fields: The fields to render
    :param hyphens: The number of hyphens to prefix field names with
    :return: The HTML
    """
    r = []
    h = "-&nbsp;" * hyphens
    for f in fields:
        # The code list and rules will have hyperlinks added to them
        # The format field might have a special format -- this is the case for the message sender and message recipient
        # fields
        r.append(cleandoc(f"""
        <tr>
            <td>{h} {f.field}</td>
            <td>{f.required}</td>
            <td>{special_formats.get(f.field, f.format)}</td>
            <td>{render_optional_code_list(f.code_list)}</td>
            <td>{create_rules(f.rules)}</td>
        </tr>"""))

    return "".join(r)


def render_type(categories: list[MessageCategory]) -> str:
    """
    Renders a message type in its entirety

    :param categories: The categories for the message type
    :return: The HTML
    """
    rows = "".join(map(lambda x: render_category_row(x), categories))
    return head_tag + header_row + rows + tail


def write_message_type_file(message_type: str, categories: list[MessageCategory]):
    """
    Writes the message type categories to a file named "messagetypes/_IExxx.md"
    :param message_type: The message type
    :param categories: The categories to render
    :return: None
    """
    file_name = f"_{message_type}_table.md"
    if not path.exists(save_location):
        os.makedirs(save_location)
    print(f"Writing file {file_name}")
    with open(file=path.join(save_location, file_name), mode="w") as md_file:
        md_file.write(render_type(categories))


# ---- Rendering for Rules

_replace_line_break_regex = re.compile(r"([A-Za-z0-9]{2}[:.])\n")


def process_rule_string(string: str, preserve_all_line_breaks = True) -> str:
    string = string.replace("<", "&lt;").replace(">", "&gt;")
    if preserve_all_line_breaks:
        string = string.replace("\n", "<br />\n")
    else:
        # only preserve those preceded by a full stop -- in which case we emulate paragraphs with spacing a bit better
        string = re.sub(_replace_line_break_regex, r"\1<br /><br />\n", string)

    return replace_code_list_full_string(string.replace("*", "<span>&#42;</span>"))


specific_line_break_rules: list[str] = []


def should_replace_line_breaks(rule_code: str) -> bool:
    if rule_code.upper().startswith("C"):
        return True
    else:
        return specific_line_break_rules.__contains__(rule_code.upper())


def render_rule(rule: Rule) -> str:
    """
    Renders a single rule in markdown
    :param rule: The rule to render
    :return: The markdown
    """
    func = process_rule_string(rule.functional_description, should_replace_line_breaks(rule.rule_code))
    tech = process_rule_string(rule.technical_description)
    return cleandoc(
        f"""## {rule.rule_code}
    
    **Functional Description**
    
    {func}
    
    **Technical Description**
    
    {tech}
    """).replace("    ", "")  # cleandoc/dedent doesn't want to work, so just do it manually


def render_rules(rules: list[Rule]) -> str:
    """
    Renders rules in markdown and joins them together
    :param rules: The rules to render
    :return: The rendered rules
    """
    return "\n\n".join(map(lambda x: render_rule(x), rules))


def write_rules_file(category: str, rules: list[Rule]):
    """
    Writes the rules for a given category to a markdown file named "rules/_rules_X.md"
    :param category: The rule category, a single letter
    :param rules: The rules to render
    :return: None
    """
    file_name = f"_rules_{category}.md"
    print(f"Writing file {file_name}")
    if not path.exists(save_location):
        os.makedirs(save_location)
    with open(file=path.join(save_location, file_name), mode="w") as md_file:
        md_file.write(render_rules(rules))
