import csv

def format(text):
    return text.replace('<', '&lt;').replace('>', '&gt;').replace('\n', '<br/>').replace('•', '- ')

prefixes = ['b','c','e','g','r','s','t']

for prefix in prefixes:
    with open(f"rules-{prefix}.html.md.erb", "wt") as writer:
        writer.write(f"""---
title: NCTS Phase 5 Technical Interface Specification
weight: {prefixes.index(prefix)+5}
description: Software developers, designers, product owners or business analysts. Integrate your software with the ERMIS service
---
#Rules {prefix.upper()}
Based on document version 5.15.0-v0.10 and issue date 04/03/2022
<%= partial 'documentation/partials/rulesintro' %>
""")

with open('q2.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        if row[0].isdigit():
            id = row[1]
            prefix = id[0].lower()
            with open(f"rules-{prefix}.html.md.erb", "at") as writer:
                writer.write(f"##{id}\n\n")
                writer.write(f"<b>Functional Description</b>\n\n")
                writer.write(f"{format(row[2])}\n\n")
                writer.write(f"<b>Technical Description</b>\n\n")
                writer.write(f"{format(row[3])}\n\n")
