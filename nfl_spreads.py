from bs4 import BeautifulSoup
import requests
import parser

URL = "http://www.footballlocks.com/nfl_point_spreads.shtml"

def remove_at(name):
    return name.replace('At', '')

if __name__ == "__main__":

    response = requests.get(URL)
    soup = BeautifulSoup(response.text, features = 'xml')
    tables = soup.find_all('table', cols = '4', width = '580')
    rows = tables[0].find_all('tr')

    header = True
    for row in rows:
        cells = row.find_all('td')
        if header:
            print(f'{cells[1].text:<15} | {cells[3].text:<15} | {cells[2].text}')
            header = False
            continue

        favorite = remove_at(cells[1].text)
        spread = float(cells[2].text)
        underdog = remove_at(cells[3].text)

        print(f"{favorite:<15} | {underdog:<15} | {spread:.1f}")
