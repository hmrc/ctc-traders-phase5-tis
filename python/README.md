# Python 3.9 Script for converting the DDNTA Q2 PDF

The Python scripts in this directory take in the DDNTA Q2 PDF file, scrapes them for appropirate message types and the rules, and converts them into TIS friendly HTML/Markdown.

In particular, this script will:

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

## Running the script

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

## Customising the behaviour of this script

This script has been designed to be semi-modular and extensible, such that the rendering logic is separate(ish) from the main code -- it's just a case of swapping out rendering functions for whatever format you wish to use -- for example, a CSV file writer. It is currently set up to only handle external domain messages.

The main script, `main.py`, augmented by `data_types.py`, will generate `MessageCategory` (with child `MessageFields`) and `Rule` objects that can then be manipulated as required.

### Controlling the output message types

The array `expected_message_types` in `main.py` determines which message types will be output by the script. Add/remove message types as required from this list.

### Controlling customised message formats

The dict `special_formats` in `render.py` will take data item names, and if it matches a key in the dict, the associated value in the `dict` will be used instead of the value in the Q2 PDF. Adding field names to this dict will allow for additional customisations to the format field.

### Controlling line breaks in functional rules

When rendering the rules, the `C` functional rules will have line breaks added wherever seen in the PDF. Other functional rules are set up to only have line breaks added when a line break is found after a full stop -- if you need to add line breaks for specific rules wherever they are in the PDF, add them, to `specific_line_break_rules` in `render.py`