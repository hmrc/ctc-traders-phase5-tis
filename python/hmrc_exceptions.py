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
from typing import Optional

from data_types import MessageCategory, Rule


def find_category(message_type: str, path: list[str], categories: list[MessageCategory]) -> MessageCategory:
    # we iterate through the list to find the various categories
    iterable_category = iter(categories)
    next(iterable_category)
    current: Optional[MessageCategory] = None
    for i in range(0, len(path)):
        level = i + 1
        # find the category in the list at the appropriate level
        cur_path = path[i]
        while True:
            current = next(iterable_category)
            if current is StopIteration or current.level < level:
                # We've gone beyond the iterator, or we have stepped back to a level in the hierarchy before
                # the level we're looking for. As a result, this is a failure
                msg = f"{message_type}: could not find {path} (was looking for level {level} item {cur_path})"
                raise RuntimeError(msg)

            elif current.level == level and current.category_name_only.lower() == cur_path.lower():
                # We found the section, so we now need to move on to the next part of the path
                # (break breaks out of the while loop, and will then continue the for loop)
                break

    # At this point, we're done, we found what we're looking for.
    return current


def set_to_optional(message_type: str, path: list[str], message_category: list[MessageCategory]):
    # we iterate through the list to find the various categories
    # noting that Python is pass by reference, we know this will be reflected back
    cat = find_category(message_type, path, message_category)
    cat.required = "O"


def message_category_transformation(message_type: str, message_category: list[MessageCategory]):
    if message_type == "IE025":
        set_to_optional(message_type, ["CONSIGNMENT", "HOUSE CONSIGNMENT", "CONSIGNMENT ITEM", "COMMODITY", "GOODS MEASURE"], message_category)

    if message_type == "IE029":
        set_to_optional(message_type, ["CONSIGNMENT", "PLACE OF LOADING"], message_category)
        set_to_optional(message_type, ["CONSIGNMENT", "HOUSE CONSIGNMENT", "CONSIGNMENT ITEM", "COMMODITY", "GOODS MEASURE"], message_category)

    if message_type == "IE043":
        set_to_optional(message_type, ["CONSIGNMENT", "HOUSE CONSIGNMENT", "CONSIGNMENT ITEM", "COMMODITY", "GOODS MEASURE"], message_category)


def rule_transformation(rule: Rule):
    if rule.rule_code == "E1104":
        rule.technical_description = rule.technical_description.replace("/*/Consignment/ActiveBorderTransportmeans/conveyanceReferenceNumber AND\n", "")
