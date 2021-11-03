from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

URL = "https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/?sortcol=td&sortdir=descending"

if __name__ == "__main__":

    response = urllib.request.urlopen(URL)
    soup = BeautifulSoup(response.read(), 'html.parser')
    tables = soup.find_all('tr')[1:21]
    top_twenty = []

    for row in tables:

        stats = {}
        player_name = row.select('a')[1].contents[0]
        player_position = row.select('span')[2].contents[0].strip()
        player_team = row.select('span')[3].contents[0].strip()
        passing_yards = row.select('td')[5].contents[0].strip()
        passing_touchdowns = row.select('td')[8].contents[0].strip()
        stats['Name'] = player_name
        stats['Position'] = player_position
        stats['Team'] = player_team
        stats['Passing Yards'] = passing_yards
        stats['Passing Touchdowns'] = passing_touchdowns
        top_twenty.append(stats)

    tables = pd.DataFrame(top_twenty)
    tables.index += 1
    print('Top 20 Players: ')
    print(tables)