import requests
from bs4 import BeautifulSoup as bs
import re
from player import Player
from config import config

class Team():
    def __init__(self, url):
        self.url = url
    @property
    def players(self):
        players = []
        headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
        url  = self.url

        html = requests.get(url, headers=headers)
        soup = bs(html.content, features=("html.parser"))
        soup = soup.select('.responsive-table > .grid-view > .items > tbody')[0]

        for cells in soup.find_all(True, {"class": re.compile("^(even|odd)$")}):
            player = Player()
            player.shirt_number = cells.find_all('td')[0].text
            player.name = cells.find_all('td')[5].text
            player.position = cells.find_all('td')[4].text
            player.age = cells.find_all('td')[6].text.split('(')[-1][:-1]    
            players.append(player)
        return players