import sys
import urllib.request as request
import urllib.error
from bs4 import BeautifulSoup as bs

def print_spreads(spreads):

    print("NFL Spread:s\n")
    print("{:<20} {:<20} {:>6}".format('Favorite', 'Underdog', 'Spread'))

    for spread in spreads:
        print("{:<20} {:<20} {:>6}".format(spread[0], spread[1], spread[2]))

def get_html(url):
    response = request.urlopen(url).read()
    html = bs(response, 'lxml')

    return html


def get_spreads(html):

    tables = html.find_all('table', attrs = { 'cols': '4', 'width': '580', 'border': '0','cellspacing': '6','cellpadding': '3'})
    rows = [row for rows in [ table.select('tr') for table in tables ] for row in rows]

    spreads = ((cell[1].text.replace("\n", " "), cell[3].text.replace("\n", " "), cell[2].text) for cell in [row.select('td:not([width])') for row in rows if row.select('td:not([width])')])
    return spreads


def main():
    url = 'http://www.footballlocks.com/nfl_point_spreads.shtml'
    html = get_html(url)
    spreads = get_spreads(html)
    print_spreads(spreads)
    sys.exit()


if __name__ == '__main__':
    main()
