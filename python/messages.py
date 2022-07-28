import bs4 as bs
import re
import copy
import itertools
import utils

class MessageSection():

    def __init__(self, messageType):
        self.messageType = messageType
        print(f"Processing message: {messageType}")

    # Process a single message type ====
    def process(self, messageTypeTag):
        htmlString = ""
        html = bs.BeautifulSoup()
        tag = messageTypeTag.find_next_sibling()

        while tag is not None and not tag.name == 'h1':
            self.processMessageTypeTags(tag, html)
            tag = tag.find_next_sibling()

        utils.joinTables(html)
        utils.swapRepeatMandatory(html.findAll('table')[1])
        utils.singleStructure(html)
        utils.fixRules(html)
        utils.rulesToLinks(html)
        utils.indent(html)

        code = utils.insertHeadings(html)
        messageName = utils.getMessageName(html)

        if code.startswith('CC'):
            #remove second table for Tranche 3 docs release
            # html.findAll("table")[1].extract()
            htmlString = f"## {self.messageType} {messageName.title()}\n{html.prettify()}"

        return htmlString

    def processMessageTypeTags(self, tag, html):
        if tag.name == 'p' and tag.text.strip() != '':
            table = self.convertPtoTable(tag, html)
            html.append(table) if table else None
                
        elif tag.name == 'h2':
            table = self.convertH2toTable(tag, html)
            html.append(table) if table else None
                    
        elif tag.name == 'table':
            html.append(self.tidyTable(copy.copy(tag), html)) if not self.isPageHeaderTable(tag) else None

    def isPageHeaderTable(self,table):
        return table.find('td').text.startswith('DDNTA for NCTS')

    def tidyMultiplePs(self, table, soup):
        for tr in table.findAll('tr'):
            tds = tr.findAll('td')
            length = len(tds[0].findAll('p')) if len(tds) > 1 else 0
                
            if length > 1:
                for i in reversed(range(length)):
                    newtr = soup.new_tag('tr')
                    tr.insert_after(newtr)
                    [self.tidyParagraphs(soup, td, i, newtr) for td in tds]
                tr.extract()

    def tidyParagraphs(self, soup, td, i, newtr):
        newtd = soup.new_tag('td')
        ps = td.findAll('p')
        newtd.string = ps[i].text if len(ps) > i else ""
        newtr.append(newtd)

    def splitColspan(self, table, soup):
        colspanCells = lambda tag: tag.name == "td" and len(tag.attrs) >= 1 and tag.has_attr("colspan")
        for td in table.findAll(colspanCells):
            count = int(td.get("colspan"))
            td['colspan'] = 1
            [td.insert_after(soup.new_tag('td')) for i in range(count-1)]

        rowspanCells = lambda tag:tag.name == "td" and len(tag.attrs) >= 1 and tag.has_attr("rowspan")

        for td in table.findAll(rowspanCells):
            td['rowspan'] = 1

    def tidyTable(self,table, soup):
    #     - multiple p tags in a single td to multiple rows
        self.tidyMultiplePs(table, soup)
    #     - orphaned rules to row above
    #     - split colspan tds
        self.splitColspan(table, soup)
        return table

    def convertH2toTable(self, h2, soup):
        name = h2.text
        table = soup.new_tag('table')
        tr = soup.new_tag('tr')
        table.append(tr)
        td = soup.new_tag('td')
        td.string = name
        tr.append(td)

        itertools.repeat(tr.append(soup.new_tag('td')), 4)

        return table

    def findMandatoryIndex(self, elements):
        for i in range(len(elements)):
            if re.match("^(M|O|R)$", elements[i]):
                return i

    def findRepeatableIndex(self, elements):
        for i in range(len(elements)):
            if re.match("(.*)x", elements[i]):
                return i

    def createTableCell(self, soup, tr, details, prop):
        td = soup.new_tag('td')
        td.string = details[prop]
        tr.append(td)

    def createDetailsA(self, elements, index): 
        return {
            'name': ' '.join(elements[0:index]).strip(),
            'repeat': elements[index],
            'mandatory': '' if len(elements) <= index+1 else elements[index+1],
            'rules': '' if len(elements) <= index+2 else ' '.join(elements[index+2:])
        }

    def createDetailsB(self, elements, index): 
        return {
            'name': ' '.join(elements[0:index]).strip(),
            'mandatory': elements[index],
            'format': elements[index+1],
            'rules': '' if len(elements) < index+3 else ' '.join(elements[index+2:])
        }

    def convertPTOTableA(self, soup, elements, index):
        table = soup.new_tag('table')
        tr = soup.new_tag('tr')
        table.append(tr)

        details = self.createDetailsA(elements, index)

        self.createTableCell(soup, tr, details, 'name')
        self.createTableCell(soup, tr, details, 'repeat')
        self.createTableCell(soup, tr, details, 'mandatory')
        self.createTableCell(soup, tr, details, 'rules')

        return table

    def convertPTOTableB(self, soup, elements, index):
        table = soup.new_tag('table')
        tr = soup.new_tag('tr')
        table.append(tr)

        details = self.createDetailsB(elements, index)

        td = soup.new_tag('td')
        tr.append(td)
        p = soup.new_tag('p')
        p['class'] = 's5'
        p.string = details['name']
        td.append(p)

        self.createTableCell(soup, tr, details, 'mandatory')
        self.createTableCell(soup, tr, details, 'format')
        self.createTableCell(soup, tr, details, 'rules')

        tr.append(soup.new_tag('td'))
        return table


    def convertPtoTable(self, p, soup):
        elements = [a for a in p.text.split(' ') if a != '']
        index = self.findRepeatableIndex(elements)
        if index:
            return self.convertPTOTableA(soup, elements, index)
        else:
            index = self.findMandatoryIndex(elements)
            if index:
                return self.convertPTOTableB(soup, elements, index)

        


