import bs4 as bs
import re
import json

def findTextUntil(startTag, endRegex):
    s = ''
    tag = startTag
    while tag is not None:
        if re.match(endRegex, tag.text):
            s = s+tag.text.replace("Functional Description", "")
            return s.replace('<', "[").replace('>', "]").strip()
        else:
            s = s + tag.text
            tag = tag.findNext('p')
    return s

def findFuncHeaderTag(startTag, endRegex):
    tag = startTag
    while tag is not None:
        if re.match(endRegex, tag.text):
            return tag
        tag = tag.findNext('p')

def removeHeader(s):
    return s.split(":")[1]

def getIssueDate(soup):
    p = soup.find('p', text=re.compile("Issue Date:(.*)"))
    return p.text.replace("Issue Date:", '').strip()

def getVersion(soup):
    p = soup.find('p', text=re.compile("Release:(.*)"))
    return p.text.replace("Release:", '').strip()

filename='q2.1.html'
soup = bs.BeautifulSoup(open(filename).read(), features="html.parser")
functionalHeader = re.compile("(.*)Functional Description:(.*)")
technicalHeader = re.compile("(.*)Technical Description:(.*)")
rules = []
for techDescHeaderTag in soup.findAll('p', text=technicalHeader):
    technical = findTextUntil(techDescHeaderTag, functionalHeader)
    funcDescHeaderTag = findFuncHeaderTag(techDescHeaderTag, functionalHeader)
    functional = findTextUntil(funcDescHeaderTag, technicalHeader)
    rules.append( {
        'name': techDescHeaderTag.text.split()[0],
        'rules': {
            'technical': removeHeader(technical),
            'functional': removeHeader(functional)
        }
    } )

# print(json.dumps(rules, indent=4, sort_keys=True))
s = ''
for rule in rules:
    s = f"{s}\n##{rule['name']}"
    s = f"{s}\n###Technical Rules"
    s = f"{s}\n{rule['rules']['technical']}"
    s = f"{s}\n###Functional Rules"
    s = f"{s}\n{rule['rules']['functional']}"

issueDate = getIssueDate(soup)
documentVersion = getVersion(soup)

d = f"---\ntitle: NCTS Phase 5 Technical Interface Specification\nweight: 5\ndescription: Software developers, designers, product owners or business analysts. Integrate your software with the ERMIS service\n---\n"
d=d+f"#Rules\n"
d=d+f"Based on document version {documentVersion} and issue date {issueDate}\n"
d=d+f"<%= partial 'documentation/partials/rulesintro' %>\n{s}"
with open("rules.html.md.erb", "w") as file:
    file.write(d)
