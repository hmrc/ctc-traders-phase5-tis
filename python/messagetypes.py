import bs4 as bs
import re
import copy

filename='q2.1.html'
validMessageTypes = [
    'IE004', 'IE007', 'IE009', 'IE013', 'IE014', 'IE015', 'IE017', 'IE019', 'IE022', 'IE023', 'IE025', 'IE028', 'IE029', 'IE035', 'IE040', 'IE042', 'IE043', 'IE044', 'IE045', 'IE048', 'IE051', 'C054', 'C055', 'C056', 'IE057', 'IE060', 'IE140', 'IE141', 'IE170', 'IE182', 'IE190', 'IE191', 'IE228', 'IE906', 'IE917', 'IE928'
]

def findMandatoryIndex(elements):
    for i in range(len(elements)):
        if re.match("^(M|O|R)$", elements[i]):
            return i

def findRepeatableIndex(elements):
    for i in range(len(elements)):
        if re.match("(.*)x", elements[i]):
            return i

def convertH2toTable(h2, soup):
    name = h2.text
    table = soup.new_tag('table')
    tr = soup.new_tag('tr')
    table.append(tr)
    td = soup.new_tag('td')
    td.string = name
    tr.append(td)
    tr.append(soup.new_tag('td'))
    tr.append(soup.new_tag('td'))
    tr.append(soup.new_tag('td'))
    tr.append(soup.new_tag('td'))
    return table


def convertPtoTable(p, soup):
    elements = [a for a in p.text.split(' ') if a != '']
    index = findRepeatableIndex(elements)
    if index:
        details = {
            'name': ' '.join(elements[0:index]).strip(),
            'repeat': elements[index],
            'mandatory': '' if len(elements) <= index+1 else elements[index+1],
            'rules': '' if len(elements) <= index+2 else ' '.join(elements[index+2:])
        }
        table = soup.new_tag('table')
        tr = soup.new_tag('tr')
        table.append(tr)
        td = soup.new_tag('td')
        td.string = details['name']
        tr.append(td)
        td = soup.new_tag('td')
        td.string = details['repeat']
        tr.append(td)
        td = soup.new_tag('td')
        td.string = details['mandatory']
        tr.append(td)
        td = soup.new_tag('td')
        td.string = details['rules']
        tr.append(td)
        return table
    else:
        index = findMandatoryIndex(elements)
        if index:
            details = {
                'name': ' '.join(elements[0:index]).strip(),
                'mandatory': elements[index],
                'format': elements[index+1],
                'rules': '' if len(elements) < index+3 else ' '.join(elements[index+2:])
            }
            table = soup.new_tag('table')
            tr = soup.new_tag('tr')
            table.append(tr)
            td = soup.new_tag('td')
            tr.append(td)
            p = soup.new_tag('p')
            p['class'] = 's5'
            p.string = details['name']
            td.append(p)
            td = soup.new_tag('td')
            td.string = details['mandatory']
            tr.append(td)
            td = soup.new_tag('td')
            td.string = details['format']
            tr.append(td)
            td = soup.new_tag('td')
            td.string = details['rules']
            tr.append(td)
            tr.append(soup.new_tag('td'))
            return table

def isPageHeaderTable(table):
    return table.find('td').text.startswith('DDNTA for NCTS')

def mergeTables(target, source):
    for tr in source.findAll('tr'):
        target.append(tr)

def isStartTable(table):
    return table.find('td').text.strip() == 'MESSAGE'

def joinTables(html):
    lastTable = None
    for table in html.findAll('table'):
        if isStartTable(table):
            lastTable = table
        else:
            if lastTable is not None:
                mergeTables(lastTable, table)
                table.extract()

def tidyMultiplePs(table, soup):
    for tr in table.findAll('tr'):
        tds = tr.findAll('td')
        if len(tds) > 1:
            length = len(tds[0].findAll('p'))
            if length > 1:
                for i in reversed(range(length)):
                    newtr = soup.new_tag('tr')
                    tr.insert_after(newtr)
                    for td in tds:
                        newtd = soup.new_tag('td')
                        ps = td.findAll('p')
                        if len(ps) > i:
                            newtd.string = ps[i].text
                        newtr.append(newtd)
                tr.extract()

def splitColspan(table, soup):
    for td in table.findAll(lambda tag:tag.name == "td" and
                len(tag.attrs) >= 1 and
                tag.has_attr("colspan")):
        count = int(td.get("colspan"))
        td['colspan'] = 1
        for i in range(count-1):
            td.insert_after(soup.new_tag('td'))
    for td in table.findAll(lambda tag:tag.name == "td" and
                len(tag.attrs) >= 1 and
                tag.has_attr("rowspan")):
        td['rowspan'] = 1

def tidyTable(table, soup):
#     - multiple p tags in a single td to multiple rows
    tidyMultiplePs(table, soup)
#     - orphaned rules to row above
#     - split colspan tds
    splitColspan(table, soup)
    return table

def singleStructure(html):
    tables = html.findAll('table')
    structure = tables[1]
    fields = tables[2]
    for tr in structure.findAll('tr'):
        name = tr.find('td').text.strip()
        for fieldtr in fields.findAll('tr'):
            if fieldtr.find('td').text.strip() == name:
                fieldtr.insert_before(tr)
                fieldtr.extract()
    structure.extract()

def insertHeadings(html):
    tables = html.findAll("table")
    tr = html.new_tag('tr')
    table = tables[0]

    xmlCell = table.find('tr').findAll('td')[1]
    name = xmlCell.text.strip('()')
    a = html.new_tag('a', href='https://github.com/hmrc/transit-movements-validator/blob/main/conf/xsd/'+name.lower()+'.xsd')
    a.string = name
    xmlCell.string = ''
    xmlCell.append(a)

    shortNameCell = table.find('tr').findAll('td')[3]
    shortNameCell.string = shortNameCell.text.strip('()')

    table.find('tr').insert_before(tr)
    td = html.new_tag('th')
    td.string = 'Message Type'
    tr.append(td)
    td = html.new_tag('th')
    td.string = 'XML Root'
    tr.append(td)
    td = html.new_tag('th')
    td.string = 'Name'
    tr.append(td)
    td = html.new_tag('th')
    td.string = 'Short Name'
    tr.append(td)
    for td in table.findAll('td'):
        td['style'] = ''
    for p in table.findAll('p'):
        p['style'] = ''

    table = tables[1]
    tr = html.new_tag('tr')
    table.find('tr').insert_before(tr)
    td = html.new_tag('th')
    td.string = 'Field Name'
    tr.append(td)
    td = html.new_tag('th')
    td.string = 'Required'
    tr.append(td)
    td = html.new_tag('th')
    td.string = 'Format / Max Repeat'
    tr.append(td)
    td = html.new_tag('th')
    td.string = 'Transition Rules'
    tr.append(td)
    td = html.new_tag('th')
    td.string = 'Business Rules'
    tr.append(td)
    for td in table.findAll('td'):
        td['style'] = ''
    for p in table.findAll('p'):
        p['style'] = ''

    return name

def swapRepeatMandatory(table):
    for tr in table.findAll('tr'):
        tds = tr.findAll('td')
        tds[1].insert_before(tds[2])

def fixRules(html):
    table = html.findAll('table')[1]
    for tr in table.findAll('tr'):
        tds = tr.findAll('td')
        for i in range(5-len(tds)):
            td = html.new_tag('td')
            tr.append(td)

        tds = tr.findAll('td')

        for rule in tds[3].text.split(' '):
            if not rule.startswith('CL'):
                tds[4].string = f"{rule} {tds[4].text}"
                tds[3].string = f"{tds[3].text.replace(rule, '')}"

def fixRepeats(html):
    ps = html.find_all('p', text=re.compile("^([0-9]x [0-9]x)$|^([0-9]x [0-9]x [0-9]x)$"))
    for p in ps:
        for r in p.text.split(' '):
            new_p = html.new_tag('p')
            new_p.string = r
            p.insert_after(new_p)
        p.extract()

def fixMandatories(html):
    ps = html.find_all('p', text=re.compile("^(R R)$|^(R R R)$"))
    for p in ps:
        for r in p.text.split(' '):
            new_p = html.new_tag('p')
            new_p.string = 'R'
            p.insert_after(new_p)
        p.extract()

def ruleLinks(html, rules):
    links = []
    for rule in rules.split(' '):
        if rule is not None and rule.strip() != '':
            a = html.new_tag('a', href=f"rules.html#{rule.lower()}")
            a.string = rule
            links.append(a)
            links.append(html.new_tag('div'))
    return links

def rulesToLinks(html):
    table = html.findAll('table')[1]
    for tr in table.findAll('tr'):
        tds = tr.findAll('td')
        rules = tds[3].text
        tds[3].string = ''
        tds[3].extend(ruleLinks(html, rules))
        rules = tds[4].text
        tds[4].string = ''
        tds[4].extend(ruleLinks(html, rules))

def indent(html):
    table = html.findAll('table')[1]
    indent = '--'
    for tr in table.findAll('tr'):
        name = tr.find('td').text
        if name == 'MESSAGE':
            indent = '--'
        elif name.startswith('-'):
            count = name.count('-')
            indent = '-' * (count+2)
        else:
            tr.find('td').string = indent+name

def getMessageName(html):
    return html.find('table').findAll('td')[2].text

def getIssueDate(soup):
    p = soup.find('p', text=re.compile("Issue Date:(.*)"))
    return p.text.replace("Issue Date:", '').strip()

def getVersion(soup):
    p = soup.find('p', text=re.compile("Release:(.*)"))
    return p.text.replace("Release:", '').strip()

soup = bs.BeautifulSoup(open(filename).read(), features="html.parser")
fixRepeats(soup)
fixMandatories(soup)
s = ""
for messageTypeTag in soup.find_all('h1', text=re.compile("2. Message Structure for: (.*)")):
    messageType = messageTypeTag.text[-5:]
    messageNumber = int(messageTypeTag.text[-3:])+3
    if messageType in validMessageTypes:
        # print(messageType)
        html = bs.BeautifulSoup()
        tag = messageTypeTag.find_next_sibling()
        while tag is not None and not tag.name == 'h1':
            if tag.name == 'p' and tag.text.strip() != '':
                table = convertPtoTable(tag, html)
                if table:
                    html.append(table)
            elif tag.name == 'h2':
                    table = convertH2toTable(tag, html)
                    if table:
                        html.append(table)
            elif tag.name == 'table':
                if not isPageHeaderTable(tag):
                    html.append(tidyTable(copy.copy(tag), html))
            tag = tag.find_next_sibling()
        joinTables(html)
        swapRepeatMandatory(html.findAll('table')[1])
        singleStructure(html)
        fixRules(html)
        rulesToLinks(html)
        indent(html)
        code = insertHeadings(html)
        messageName = getMessageName(html)
        if code.startswith('CC'):
            #remove second table for Tranche 3 docs release
            # html.findAll("table")[1].extract()
            s = f"{s}\n## {messageType} {messageName.title()}\n{html.prettify()}"
        # else:
            # print(f"ignoring {messageType} ({code})")
    # else:
        # print(f"ignoring {messageType}")

issueDate = getIssueDate(soup)
documentVersion = getVersion(soup)
d = f"---\ntitle: NCTS Phase 5 Technical Interface Specification\nweight: 4\ndescription: Software developers, designers, product owners or business analysts. Integrate your software with the ERMIS service\n---\n"
d=d+f"#Message types\n"
d=d+f"Based on document version {documentVersion} and issue date {issueDate}\n"
d=d+f"<%= partial 'documentation/partials/messagetypeintro' %>\n"
d=d+s
with open("messagetypes.html.md.erb", "w") as file:
    file.write(d)
