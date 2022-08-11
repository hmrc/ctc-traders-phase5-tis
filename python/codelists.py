import csv
import os

ignored = ['CL060']

codelists = []
with open('codelists.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        codelists.append(row)
folder = os.getcwd()+'/../source/documentation/partials/'
for filename in os.listdir(folder):
    if filename.startswith("_IE") and filename.endswith(".md"):
        with open(folder+filename, "rt") as file:
            with open(filename, "wt") as out:
                text = file.read()
                for row in codelists:
                    cl = row[0].strip()
                    link = f"<a href='{row[2]}'>{cl}</a>"
                    if cl not in ignored:
                        text = text.replace(cl, link)
                    else:
                        print(f"ignoring {cl}")
                out.write(text)
