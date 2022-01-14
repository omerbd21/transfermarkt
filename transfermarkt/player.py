import requests
import settings
from bs4 import BeautifulSoup as bs
import csv

class Player():
    def __init__(self):
        self.player_data = {}
        self.stats = []

    def player_to_json(self):
        return self.player_data
    
    def stats_to_csv(self):
        self.get_stats()
        with open(self.player_data["name"] + ".csv", "w") as f:
            w = csv.writer(f)
            for row in self.stats:
                w.writerow(row)
    @property
    def shirt_number(self):
        return self.player_data["shirt_number"]
    @shirt_number.setter
    def shirt_number(self, number):
        self.player_data["shirt_number"] = number
    
    
    @property
    def name(self):
        return self.player_data["name"]
    @name.setter
    def name(self, name):
        self.player_data["name"] = name
    
    
    @property
    def position(self):
        return self.player_data["position"]
    @position.setter
    def position(self, position):
        self.player_data["position"] = position
    

    @property
    def age(self):
        return self.player_data["age"]
    @age.setter
    def age(self, age):
        self.player_data["age"] = age
    
    @property
    def player_link(self):
        return self.player_data["player_link"]
    @player_link.setter
    def player_link(self, player_link):
        self.player_data["player_link"] = player_link
    
    def get_stats(self):
        html = requests.get(self.player_link, headers=settings.HEADERS)
        soup = bs(html.content, features=("html.parser"))
        table = soup.select('table.items')[0]
        columns = table.find_all('th')
        parameters = ['']
        for column in columns:
            a = column.find('a')
            if a:
                span = a.find('span')
                if span:
                    parameters.append(span.get('title'))
        self.stats.append(parameters)
        rows = table.find_all('tr')
        stat_1, stat_2, stat_3, stat_4, stat_5 = [], [], [], [], []
        competitions = []
        for row in rows:
            if len(row.find_all('td')) > 1:
                competitions.append(row.find_all('td')[1].text.strip())
                stat_1.append(row.find_all('td')[2].text)
                stat_2.append(row.find_all('td')[3].text)
                stat_3.append(row.find_all('td')[4].text)
                stat_4.append(row.find_all('td')[5].text)
                stat_5.append(row.find_all('td')[6].text)
        stat_1 = stat_1[1:]
        stat_2 = stat_2[1:]
        stat_3 = stat_3[1:]
        stat_4 = stat_4[1:]
        stat_5 = stat_5[1:]
        competitions = list(filter(None, competitions))
        for c, s1, s2, s3, s4, s5 in zip(competitions, stat_1, stat_2, stat_3, stat_4, stat_5):
            stats = [c, s1, s2, s3, s4, s5]
            self.stats.append(stats)
        return self.stats