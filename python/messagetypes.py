import bs4 as bs
import re
import messages

filename='q2.1.html'
validMessageTypes = [
    'IE004', 'IE007', 'IE009', 'IE013', 'IE014', 'IE015', 'IE019', 'IE022', 'IE025', 'IE028', 'IE029', 'IE035', 'IE043', 'IE044', 'IE045', 'IE051', 'IE055', 'IE056', 'IE057', 'IE060', 'IE170', 'IE182', 'IE917', 'IE928'
]

def fixRepeats(html):
    fix(html, "^([0-9]x [0-9]x)$|^([0-9]x [0-9]x [0-9]x)$", None)

def fixMandatories(html):
    fix(html, "^(R R)$|^(R R R)$", 'R')

def fix(html, regex, item):
    ps = html.find_all('p', text=re.compile(regex))
    for p in ps:
        for r in p.text.split(' '):
            new_p = html.new_tag('p')
            new_p.string = r if item is None else item
            p.insert_after(new_p)
        p.extract()


def getIssueDate(soup):
    p = soup.find('p', text=re.compile("Issue Date:(.*)"))
    return p.text.replace("Issue Date:", '').strip()

def getVersion(soup):
    p = soup.find('p', text=re.compile("Release:(.*)"))
    return p.text.replace("Release:", '').strip()

# =============================================================================
# Main
# =============================================================================
soup = bs.BeautifulSoup(open(filename).read(), features="html.parser")
fixRepeats(soup)
fixMandatories(soup)

messageTypes = []

# Iterate round each message type
for messageTypeTag in soup.find_all('h1', text=re.compile("2. Message Structure for: (.*)")):
    messageType = messageTypeTag.text[-5:]
    messageNumber = int(messageTypeTag.text[-3:])+3

    if messageType in validMessageTypes:
        message = messages.MessageSection(messageType)
        htmlStr = f"{message.process(messageTypeTag)}"
        messageTypes.append(messageType)
        with open(f"_{messageType}.md", "w") as file:
            file.write(htmlStr)

    else:
        print(f"Ignoring message: {messageType}")


issueDate = getIssueDate(soup)
documentVersion = getVersion(soup)

doc = f"---\ntitle: NCTS Phase 5 Technical Interface Specification\nweight: 4\ndescription: Software developers, designers, product owners or business analysts. Integrate your software with the ERMIS service\n---\n"
doc = doc + f"#Message types\n"
doc = doc + f"Based on document version {documentVersion} and issue date {issueDate}\n"
doc = doc + f"<%= partial 'documentation/partials/messagetypeintro' %>\n"
for messageType in messageTypes:
    doc = doc + f"<%= partial 'documentation/partials/{messageType}' %>\n"

with open("messagetypes.html.md.erb", "w") as file:
    file.write(doc)
