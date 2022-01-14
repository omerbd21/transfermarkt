import requests
from bs4 import BeautifulSoup as bs
import re
from .player import Player
import settings

class Team():
    def __init__(self, url):
        self.url = url
    @property
    def players(self):
        players = []
        url  = self.url

        html = requests.get(url, headers=settings.HEADERS)
        soup = bs(html.content, features=("html.parser"))
        soup = soup.select('.responsive-table > .grid-view > .items > tbody')[0]

        for cells in soup.find_all(True, {"class": re.compile("^(even|odd)$")}):
            player = Player()
            player.shirt_number = cells.find_all('td')[0].text
            link = cells.find_all('td')[3]
            player.player_link = settings.BASE_URL + link.find_all('a')[0]['href']
            player.name = cells.find_all('td')[5].text
            player.position = cells.find_all('td')[4].text
            player.age = cells.find_all('td')[6].text.split('(')[-1][:-1]    
            players.append(player)
        return players