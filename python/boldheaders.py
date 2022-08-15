import bs4 as bs
import re
import os

r = re.compile('^\d+x')
folder = os.getcwd()+'/../source/documentation/partials/'
for filename in os.listdir(folder):
    soup = bs.BeautifulSoup(open(folder+filename).read(), features="html.parser")
    for tr in soup.findAll('tr'):
        tds = tr.findAll('td')
        if len(tds) > 3 and r.match(tds[2].text.strip()):
            tds[0].string.wrap(soup.new_tag("b"))
    with open(filename, "w") as file:
        file.write(str(soup))
