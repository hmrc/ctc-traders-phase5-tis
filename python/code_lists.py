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
import csv
from typing import Optional

# Codelist to URLs
code_lists: Optional[dict[str, str]] = None


class CodeList:
    def __init__(self, dictionary: dict):
        self.code_list = dictionary["Code List"]
        self.title = dictionary["Title"]


def load_code_list() -> dict[str, CodeList]:
    global code_lists
    if code_lists is None:
        result: dict[str, CodeList] = {}
        with open(file="code_lists.csv", mode="r") as code_list_file:
            reader = csv.DictReader(code_list_file, delimiter=",")
            for row in reader:
                code_list = CodeList(row)
                result[code_list.code_list] = code_list

        code_lists = result

    return code_lists


def replace_code_list(cl: str) -> str:
    """
    If the codelist exists in the dict, wraps the codelist in an HTML link. Else, returns the codelist
    :param cl: The codelist
    :return: The codelist, with or without a hyperlink wrapping
    """
    return cl


def replace_code_list_full_string(string: str) -> str:
    """
    Takes a string and adds links to any known codelists

    :param string: The string
    :return: The linkified string
    """
    replaced = string
    for key, item in load_code_list().items():
        replaced = replaced.replace(key, replace_code_list(key))
    return replaced
