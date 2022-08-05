import csv
from html import escape

with open('q2.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    with open("rules.html.md.erb", "w") as writer:
        writer.write("""---
title: NCTS Phase 5 Technical Interface Specification
weight: 5
description: Software developers, designers, product owners or business analysts. Integrate your software with the ERMIS service
---
#Rules
Based on document version 5.15.0-v0.10 and issue date 04/03/2022
<%= partial 'documentation/partials/rulesintro' %>
""")
        for row in reader:
            if row[0].isdigit():
                writer.write(f"##{row[1]}\n\n")
                writer.write(f"###Functional Description\n\n")
                writer.write(f"{escape(row[2])}\n\n")
                writer.write(f"###Technical Description\n\n")
                writer.write(f"{escape(row[3])}\n\n")
