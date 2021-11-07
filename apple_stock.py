import requests
from bs4 import BeautifulSoup
import urllib.request


URL = 'https://finance.yahoo.com/quote/AAPL/history?p=AAPL'
page = requests.get(URL, headers = {'User-Agent' : 'Custom'})
content = page.content
soup = BeautifulSoup(content, 'html.parser', from_encoding="utf-8")

data = soup.find_all('tr', attrs= 'BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)')
print(data)


#if __name__ == "__main__":

for row in range(len(data)):
    '''close_date = i.find_all('span')[0].text.strip()
    close_value = i.find_all('span')[4].text.strip()'''
    parse = data[row].find_all('span')
    date = parse[0].text.strip()
    open = parse[1].text.strip()

