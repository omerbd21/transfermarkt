from src import Team

t = Team('https://www.transfermarkt.com/manchester-united/startseite/verein/985')
print(t.players[26].stats_to_csv())