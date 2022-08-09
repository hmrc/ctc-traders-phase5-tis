import math

ignoredFields = [
    'Message sender'
]

# Get message name from 2nd cell in table
def getMessageName(html):
    return html.find('table').findAll('td')[2].text


# Merge tables ====
def isStartTable(table):
    return table.find('td').text.strip() == 'MESSAGE'

def mergeTables(target, source):
    [target.append(tr) for tr in source.findAll('tr')]

def joinTables(html):
    lastTable = None
    for table in html.findAll('table'):
        if isStartTable(table):
            lastTable = table
        else:
            if lastTable is not None:
                mergeTables(lastTable, table)
                table.extract()


def swapRepeatMandatory(table):
    for tr in table.findAll('tr'):
        tds = tr.findAll('td')
        tds[1].insert_before(tds[2])


# Row restructuring ====
def restructureRow(tr, fields):
    name = tr.find('td').text.strip()
    for fieldtr in fields.findAll('tr'):
        if fieldtr.find('td').text.strip() == name:
            fieldtr.insert_before(tr)
            fieldtr.extract()

def singleStructure(html):
    tables = html.findAll('table')
    structure = tables[1]
    fields = tables[2]
    [restructureRow(tr,fields) for tr in structure.findAll('tr')]
    structure.extract()


# Fix rules ====
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

# Make rule hyperlinks ====
def rulesToLinks(html):
    table = html.findAll('table')[1]
    for tr in table.findAll('tr'):
        tds = tr.findAll('td')
        rules = tds[4].text
        tds[4].string = ''
        tds[4].extend(ruleLinks(html, rules))

def ruleLinks(html, rules):
    links = []
    for rule in rules.split(' '):
        if rule is not None and rule.strip() != '':
            a = html.new_tag('a', href=f"rules.html#{rule.lower()}")
            a.string = rule
            links.append(a)
            links.append(html.new_tag('div'))
    return links

# Indent message elements in rows ====
def indent(html):
    table = html.findAll('table')[1]
    prefix = ''
    for tr in table.findAll('tr'):
        td = tr.find('td')
        name = td.text
        td.string = name.replace('---', '- ').strip()
        if name.strip() in ignoredFields:
            tr.extract()
        else:
            if name == 'MESSAGE':
                # Top level so child fields must start with a single -
                prefix = '- '
            elif name.startswith('--'):
                level = math.floor(name.count('-')/3)
                prefix = ('- ' * (level+1))
            else:
                tr.find('td').string = prefix+name


# Insert Headings for tables ====
def insertHeadings(html):
    tables = html.findAll("table")
    tr = html.new_tag('tr')

    table = tables[0]
    xmlCell = table.find('tr').findAll('td')[1]
    name = xmlCell.text.strip('()')
    messageHeaderTableHeadings(html, table, tr, name, xmlCell)

    table = tables[1]
    messageDetailsTableHeadings(html, table)

    return name

def createTableHeader(html, tr, title):
    td = html.new_tag('th')
    td.string = title
    tr.append(td)

def clearCellStyle(table):
    for td in table.findAll('td'):
        del td['style']
    for tr in table.findAll('tr'):
        del tr['style']
    del table['style']

def clearParagraphStyle(table):
    for p in table.findAll('p'):
        del p['style']

def removeEmptyDivs(table):
    for div in table.findAll('div'):
        if div.text.strip() == '':
            div.extract()

# Message Header Table ========
def messageHeaderTableHeadings(html, table, tr, name, xmlCell):
    a = html.new_tag('a', href='https://github.com/hmrc/transit-movements-validator/blob/main/conf/xsd/'+name.lower()+'.xsd')
    a.string = name
    xmlCell.string = ''
    xmlCell.append(a)

    shortNameCell = table.find('tr').findAll('td')[3]
    shortNameCell.string = shortNameCell.text.strip('()')

    table.find('tr').insert_before(tr)
    createTableHeader(html, tr, 'Message Type')
    createTableHeader(html, tr, 'XML Root')
    createTableHeader(html, tr, 'Name')
    createTableHeader(html, tr, 'Short Name')

    clearCellStyle(table)
    clearParagraphStyle(table)
    removeEmptyDivs(table)

# Message details Table ========
def messageDetailsTableHeadings(html, table):
    tr = html.new_tag('tr')
    table.find('tr').insert_before(tr)

    createTableHeader(html, tr, "Field Name")
    createTableHeader(html, tr, "Priority")
    createTableHeader(html, tr, "Format / Max Repeat")
    createTableHeader(html, tr, "Code Lists")
    createTableHeader(html, tr, "Rules")

    clearCellStyle(table)
    clearParagraphStyle(table)

