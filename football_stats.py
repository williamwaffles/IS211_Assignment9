from bs4 import BeautifulSoup
import urllib.request
import ssl

def main():
    url = 'https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/?sortcol=td&sortdir=descending'
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response.read(), features='lxml')
    player_info = soup.find_all('tr')[1:21]
    top_twenty = []

if __name__ == "__main__":
    main()