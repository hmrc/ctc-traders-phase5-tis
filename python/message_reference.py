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

message_reference: Optional[dict[str, str, str]] = None


class MessageReference:
    def __init__(self, dictionary: dict):
        self.code = dictionary["Code"]
        self.message = dictionary["Message"]
        self.reference = dictionary["Reference"]


def expected_message_references():
    result = []
    for e in load_message_reference():
        result.append(e.reference)
    return result

def expected_message_types():
    result = []
    for e in load_message_reference():
        result.append(e.code)
    return result


def load_message_reference() -> dict[str, MessageReference]:
    global message_reference
    if message_reference is None:
        result: dict[str, MessageReference] = {}
        with open(file="message_reference.csv", mode="r") as message_reference_file:
            reader = csv.DictReader(message_reference_file, delimiter=",")
            for row in reader:
                print(row)
                message_reference = MessageReference(row)
                result[message_reference] = message_reference

        message_reference = result

    return message_reference
