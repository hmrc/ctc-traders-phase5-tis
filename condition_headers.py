import sys
import bs4 as bs

if __name__ == "__main__":
    filename = sys.argv[1]
    soup = bs.BeautifulSoup(open(filename).read(), features="html.parser")
    for h1 in soup('h1'):
        for a in h1('a'):
            title = a.text
            a.extract()
            h1.string = title
    with open(filename+".headers", "w") as file:
        file.write(soup.prettify())
