import sys
import requests
from bs4 import BeautifulSoup as bs

def print_aapl(appl_close):
    print("\nApple Stock (Ticker AAPL) Closing Values:\n")
    print("{:<20}{:<10}".format('Date', 'Close Value\n'))
    for aapl in appl_close:
        print("{:<20}{:<10}".format(aapl[0], aapl[1]))

def get_html(url):
	user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
	headers = { 'User-Agent' : user_agent }
	req = requests.get(url, headers=headers).content
	html = bs(str(req), 'lxml')
	return html


def get_appl_close(html):
    rows = html.findAll('tr', attrs={'BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)'})
    appl_close=[]
    for row in rows:
        try:
            close_date = row.findAll('span')[0].text.strip()
            close_value = row.findAll('span')[4].text.strip()
            appl_close.append([close_date, close_value])
        except:
            break
    return appl_close


def main():
    url = 'https://finance.yahoo.com/quote/AAPL/history?p=AAPL'
    html = get_html(url)
    appl_close = get_appl_close(html)
    print_aapl(appl_close)
    sys.exit()

if __name__ == '__main__':
    main()
