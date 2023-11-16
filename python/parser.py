import hmrc_exceptions
from data_types import MessageField, MessageCategory, Rule
from typing import Optional, Iterator
import re
from PyPDF2 import PdfReader

regex = "Message Structure for: (IE\\d{3})"


def find_pages(reader: PdfReader, expected_message_types: list[str]) -> tuple[list[tuple[str, int, int]], int]:
    print("Scanning document...")
    l: list[tuple[str, int, int]] = list()
    current_message_type = None
    start_page = 0
    for x in range(0, len(reader.pages)):
        # For each page, we're looking for the heading
        # "Message Structure for: IExxx"
        #
        # That heading indicates a new message. The PDF reader ignores the header table, which
        # is really useful in this case.
        page = reader.pages[x]
        text = page.extract_text()
        match = re.search(regex, text)
        if match is not None and match.group(1) != current_message_type:
            # We found a header that refers to a message type that is not the current one (e.g. IE001 to IE002)
            # We start the scan from this page for the new type, and we now have the range for the previous message type
            # which we store.
            if current_message_type is not None:
                print(f"... message type {current_message_type}, pages {start_page} to {x-1}")
                l.append((current_message_type, start_page, x-1))

            # Of course, we only care about external domain types, so we ignore IE messages that are not of interest
            # to us, such as the IE001, which is common domain.
            #
            # This sets current_message_type to None if we don't care, which means we won't bother parsing it later
            if expected_message_types.__contains__(match.group(1)):
                current_message_type = match.group(1)
                start_page = x
            else:
                current_message_type = None
        elif match is None and text.__contains__("List of Rules, Conditions and Guidelines"):
            # At some point we'll finish reading the message types, and instead, we'll come across the rules
            # which starts with the header "List of Rules, Conditions and Guidelines". Once we find that,
            # we end or message type search and log the start page for the rules, which we'll use later.
            print(f"... message type {current_message_type}, pages {start_page} to {x - 1}")
            print(f"... rules start page: {x}")

            if current_message_type is not None:
                # if the last message type is one we log, make sure we get the start/end pages
                l.append((current_message_type, start_page, x - 1))
            # return both the list of message types, and the start page of the rules
            return l, x

    # If we get here, we never found the rules -- abort.
    raise EOFError


def read_message(reader: PdfReader, start: int, end: int, message_type: str) -> list[MessageCategory]:
    """
    Reads a message and parses it into memory

    For each message, the Q2 document is split into two bits of documentation: groups, and
    individual message type. Because it's a PDF, it's a bit of a mess, but it is predictable.

    We pass through the groups first, get the information, then we can attach the single items below it.

    This gives us a data structure that we can then convert into Markdown, attach links to code lists, etc. etc.

    :param reader: The PDF Reader
    :param start: First page
    :param end: Last page
    :param message_type: The message type
    :return: The categories
    """
    print(f"Reading message type: {message_type}")
    categories: list[MessageCategory] = []
    is_category_page: bool = True
    # needs to be on the outside because categories may split over pages
    category: Optional[MessageCategory] = None
    categories_iter: Optional[Iterator[MessageCategory]] = None
    field: Optional[MessageField] = None
    # for the first pages, until we encounter "MESSAGE", we have categories
    for page in range(start, end+1):
        text = reader.pages[page].extract_text().splitlines()
        # A page will EITHER contain categories, OR will contain fields, NOT BOTH
        # We can determine the boundary by looking for the word MESSAGE as the first message
        # category acts as a semaphore, once we're looking at fields for a message type, that's
        # all we'll look at until the next message type
        if text[0].strip() == "MESSAGE":
            is_category_page = False
            category = None
            categories_iter = categories.__iter__()

        if is_category_page:
            # We're processing categories
            for line in text:
                # There are lines that are headers for the message type, or wrap around and contain
                # the short name of the data type. This ignores that line
                if line.__contains__(message_type) or line.__contains__("E_"):
                    continue

                # If we're on the last lines where the page number is, no need to process further
                if line.startswith("Page"):
                    break

                # Either we have a category (starts with -), or we haven't started yet (category is None)
                # -- we start a new category in this case
                #
                # If we don't have this condition, we've got a rule to add to the existing category, so we add it
                if line.startswith("-") or category is None:
                    # new category
                    category = MessageCategory(message_type)
                    categories.append(category)
                    category.parse_line(line)
                else:
                    category.add_rule(line)
        else:
            # We're processing individual data items
            for line in text:
                if line.startswith("Page"):
                    break

                # The page will define categories starting with hyphens, except for MESSAGE, which is the first word
                # in the section. Fields will not have hyphens. We use that to be able to bundle fields with their
                # respective categories
                if line.startswith("-") or category is None:
                    # we have a category, go get it
                    category = next(categories_iter)
                elif line.strip().__contains__(" "):
                    # This is a bit of a weird rule, but essentially, the first line of a field entry will
                    # always contain a space between the field name and the requirement/format section,
                    # so we use that to determine when we have new entries.
                    field = MessageField()
                    category.add_field(field)
                    field.parse_line(line)
                else:
                    # If the line has no spaces, we're confident it's another rule for the previous field,
                    # so we just add that
                    field.add_rule(line)

    return categories


def read_and_transform(reader: PdfReader, start: int, end: int, message_type: str) -> list[MessageCategory]:
    categories: list[MessageCategory] = read_message(reader, start, end, message_type)
    hmrc_exceptions.message_category_transformation(message_type, categories)
    return categories


def extract_rules(reader: PdfReader, start_page: int) -> dict[str, list[Rule]]:
    print("Extracting rules...")
    rules: dict[str, list[Rule]] = {}
    current_buffer: Optional[list[str]] = None
    for page in range(start_page, len(reader.pages)):
        print(f"... page {page}")
        for line in reader.pages[page].extract_text().splitlines():
            if line.startswith("Page"):
                break

            # Each rule starts with the rule number, some whitespace, and then "Technical Description:", so we can
            # parse the line, and read the lines below it for the rule description
            #
            # Getting to this means the previous rule is finished, so we should package it up
            if re.match("[A-Z]\\d{4}\\s+Technical Description:", line):
                if current_buffer:
                    # The lines are done, create a Rule object which parses the rule into the various chunks
                    rule = Rule(current_buffer)
                    print(f" ... ... {rule.rule_code}")
                    # If the category (B, C etc.) doesn't exist in the dict yet, we create it, then add the
                    # rule to that category
                    rules.setdefault(rule.rule_category, []).append(rule)

                # The new buffer now contains the current line, as this is part of the rule
                current_buffer = [line]
            elif current_buffer is not None:
                # If we're not starting a new rule, just buffer the line
                current_buffer.append(line)

    # Clean up the last rule which won't have been stored yet
    rule = Rule(current_buffer)
    print(f" ... ... {rule.rule_code}")
    rules.setdefault(rule.rule_category, []).append(rule)
    print(f"Rule extraction complete")
    return rules


def filter_rules(reader: PdfReader, start_page: int, categories: list[list[MessageCategory]]) -> list[Rule]:
    list_of_ed_rules: set[Rule] = set()
    