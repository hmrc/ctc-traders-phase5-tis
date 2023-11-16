# Python 3.9 Scripts for converting the DDNTA Q2 PDF and diffing two DDNTA Q2 PDFs

The Python scripts in this directory take in the DDNTA Q2 PDF file, scrapes them for appropriate message types and the rules, and converts them into TIS friendly HTML/Markdown.

In particular, the conversion script will:

* read the selected message type data groups and data items and extract:
  * formatting notes
  * multiplicity
  * requirement
  * any associated code list and link them to the Europa or local website, if the lists are available
  * associated rules, with a link to the appropriate place in the rules section
* read the rules and conditions section and extract the rules, while:
  * linking any code lists
  * adding line breaks to the technical rules and C group functional rules where line breaks exist in the PDF
  * adding line breaks to the functional rules (except C group) where a line break exists after a full stop
* add them to the `source/documentation/partials` directory

This script will also perform a few other transformations, including

* adding a note about message sender/recipient entries for each message type

The diffing script will take two DDNTA Q2 sections and perform a diff using DeepDiff.

## Running the script - conversion

The `.gitignore` file contains an entry for `python/env`, if you create a specific virtual env for this script, use the name `env`.

Ensure you install the requirements using `pip`:

```bash
pip install -r requirements.txt
```

then run the script with a single argument pointing to the DDNTA Q2 PDF you wish to use to update the TIS (on macOS or Linux, if you use Windows adjust accordingly):

```bash
python ./main.py "/path/to/pdf/q2.pdf"
```

The script will put the generated files in `../source/documentation/partials`. You can then just view the TIS as normal and the changes will be picked up.

## `code_lists.csv`

If additional code lists need to be linked in the TIS, add them to the `code_lists.csv` file. There are three columns:

* Code list identifier
* Title
* Link

Ensure that all three bits of information are added. The script will then pick up the change and add links as appropriate.

## Customising the behaviour of the conversion script

This script has been designed to be semi-modular and extensible, such that the rendering logic is separate(ish) from the main code -- it's just a case of swapping out rendering functions for whatever format you wish to use -- for example, a CSV file writer. It is currently set up to only handle external domain messages.

The main script, `main.py`, augmented by `data_types.py`, will generate `MessageCategory` (with child `MessageFields`) and `Rule` objects that can then be manipulated as required.

### Controlling the output message types

The array `expected_message_types` in `main.py` determines which message types will be output by the script. Add/remove message types as required from this list.

### Controlling customised message formats

The dict `special_formats` in `render.py` will take data item names, and if it matches a key in the dict, the associated value in the `dict` will be used instead of the value in the Q2 PDF. Adding field names to this dict will allow for additional customisations to the format field.

### Controlling line breaks in functional rules

When rendering the rules, the `C` functional rules will have line breaks added wherever seen in the PDF. Other functional rules are set up to only have line breaks added when a line break is found after a full stop -- if you need to add line breaks for specific rules wherever they are in the PDF, add them, to `specific_line_break_rules` in `render.py`

### Adding HMRC specific changes

In the `hmrc_exceptions.py` file, the `message_category_transformation` function will take the current message type being processed and perform the transformations it needs to. Right now, only changing the priority to optional is supported, but should other differences be needed, they should be added here.

There is a `find_category` function, use this to find a specific data group based on its hierarchy should you need to create an additional transformation.

## Running the script - diffing

The `.gitignore` file contains an entry for `python/env`, if you create a specific virtual env for this script, use the name `env`.

Ensure you install the requirements using `pip`:

```bash
pip install -r requirements.txt
```

then run the script with a single argument pointing to the DDNTA Q2 PDF you wish to use to update the TIS (on macOS or Linux, if you use Windows adjust accordingly):

```bash
python ./diff.py "/path/to/old/pdf/q2.pdf" "/path/to/new/pdf/q2.pdf"
```

This will generate a `diff_result.txt` file in the working directory containing the output.

### Reading the diff results.

The results are separated into the message types and the rules. The rules are self-explanatory, it tells you:

* which rules have been added
* which rules have been removed
* whicb rules have been changed

For added and changed rules, the script will print out the old and new rules where changed.

For the message types, you'll get a slightly more Json like output that looks like this:

```text
Diff for IE015
{'dictionary_item_added': [root.node['CONSIGNMENT'].node['HOUSE CONSIGNMENT'].node['Country of destination']],
 'iterable_item_added': {"root.node['CONSIGNMENT'].node['Country of destination'].field.rules[1]": 'G0113',
                         "root.node['CONSIGNMENT'].node['Country of dispatch'].field.rules[0]": 'B2104',
                         "root.node['CONSIGNMENT'].node['HOUSE CONSIGNMENT'].node['CONSIGNMENT ITEM'].node['Country of destination'].field.rules[1]": 'G0113',
                         "root.node['CONSIGNMENT'].node['HOUSE CONSIGNMENT'].node['CONSIGNMENT ITEM'].node['Country of dispatch'].field.rules[0]": 'B2104',
                         "root.node['CONSIGNMENT'].node['HOUSE CONSIGNMENT'].node['CONSIGNMENT ITEM'].node['PREVIOUS DOCUMENT'].node['Type'].field.rules[1]": 'G0991',
                         "root.node['CONSIGNMENT'].node['HOUSE CONSIGNMENT'].node['Country of dispatch'].field.rules[0]": 'B2104',
                         "root.node['CONSIGNMENT'].node['HOUSE CONSIGNMENT'].node['PREVIOUS DOCUMENT'].node['Type'].field.rules[0]": 'G0991',
                         "root.node['CUSTOMS OFFICE OF EXIT FOR TRANSIT (DECLARED)'].category.rules[0]": 'B2102'},
 'values_changed': {"root.node['CONSIGNMENT'].node['HOUSE CONSIGNMENT'].category.multiplicity": {'new_value': '1999x',
                                                                                                 'old_value': '99x'}}}
```

This block says, for the IE015:

* under `dictionary_item_added`, the data field "CONSIGNMENT" > "HOUSE CONSIGNMENT" > "Country of destination" was added
* under `iterable_item_added`, multiple rules were added to fields and categories, for example:
  * the data item "CONSIGNMENT" > "Country of destination" now has the rule "G0113" added
  * the data group "CUSTOMS OFFICE OF EXIT FOR TRANSIT (DECLARED)" has the rule "B2102" added
* under `values_changed`, the multiplicity of the data group "CONSIGNMENT" > "HOUSE CONSIGNMENT" has changed from 99x to 1999x

You may find that code lists are also updated, these would also be under `values_changed`.

### Generating the diffs -- a note on lists vs dicts

In order to remove any potential issue with ordering, the script will turn the list of rules and list of data groups into dicts. By doing so, the diff will generate against the name of a data item/group, rather than its index, and will avoid generating false diffs when things have changed in order.

It should be noted that order is indeed important, but that'll be handled by the XSDs rather than the TIS.

# Parsing the Q2 PDF

> This section explains the technical detail of what the script expects and how it parses it. If you are just running the script, feel free to ignore this section.

This script makes use of the `PyPDF 3` library, specifically the `extract_text` function. This allows us to get rid of the various bits of formatting, but does give us a slightly mangled output. Thankfully, this output is also consistent across multiple versions of the DDNTA and so we can exploit this fact in our parsing.

## Message types, data groups, data items

In the Q2 PDF, the data groups and data items are separated, and usefully, are separated by a page break. We use this to great effect, as:

* the headers on the pages are not exposed by `extract_text`
* the data item page **always** begins with `MESSAGE`
* the data groups page starts with a title containing the message type -- this might split over two lines so we also look for `E_` to ensure we don't accidently parse a title line improperly.

We use this to be able to build up a picture of what is a data group, and what is a data item. Both have their own challenges in parsing however. In all cases, we ignore headers and complete parsing of a page when we see the "Page X" identifier.

**For data groups**, we know that either the first non-title line, or a line that begins with a hyphen, is a data group, so we then parse it as such. The line will look something like:

```
------TRANSPORT CHARGES 1xDC0186
```

The title is up to the last space, while we can extract:

* multiplicity up to and including the `x` (regex: `\d+x`)
* the next letter is the requirement status (will be R, D or O)
* the last five letters, if they exist, will be a rule (regex `[BCEGRST](\d{4})`)

Any additional rows below that don't contain hyphens will just contain additional rules for this data group.

**For data item**, we know that a category starts with a hyphen or `MESSAGE`. As the categories are in the same order here as they are in their own section, we just take our parsed categories in order and start attaching rules (see `main.py` for how we do this).

The line for data items will look something like one of the following:

```
Reference number Ran8CL172R0901 (Everything)
Binding itinerary Rn1CL027 (no rule)
Release date Ran10 G0002 (no code list)
Message recipient Ran..35 (no rule, no codelist)
```

Taking the top example, we have:

* the name of the item, followed by a space
* the next letter is the requirement status (will be R, D or O)
* a set of characters defining the format
* a code list, starting CL followed by three digits (regex `CL\d{3}`)
* the last five letters, if they exist, will be a rule (regex `[BCEGRST](\d{4})`)

Other formats exist based on the fact that code lists and rules are optional. The parser takes care of this baed on what it sees.

Like with data groups, there is the potential for multiple rules for a given item. They are presented and parsed in the same way.

**For rules**, we start parsing the rules from section 3 (List of Rules, Conditions and Guidelines). Each rule will be presented in text as 

```
B1000 Technical Description:
```

so we know the rule, and that we start with the techncial decription. We categorise based on the letter, and then store the rule details. The lines below the technical description are stored, with line breaks, as the technical description. We will then come across

```
Functional Description:
```

where we read until we come across the next rule, again storing line breaks.

This continues to the end of the file.