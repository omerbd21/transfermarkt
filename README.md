# Transfermarkt
A package to query transfermarkt, mainly aimed at statistics
## Description
The package allows developers to query tranfermarkt and get data on teams and on specific players.  
In the future, I will add a query on leagues.  

I used beautifulsoup4 to query the transfermarkt website, and of course the requests module.

## Installation

```python
pip install transfermarkt
```
As simple as that.

## Usage
Getting all players of a team:
```python
t = Team('https://www.transfermarkt.com/real-madrid/startseite/verein/418')
players = t.players
```

Getting all data on a player as dict:
```python
t = Team('https://www.transfermarkt.com/real-madrid/startseite/verein/418')
player_data = t.players[0].player_to_json()
```

Output all stats of a player to CSV:
```python
t = Team('https://www.transfermarkt.com/real-madrid/startseite/verein/418')
player_data = t.players[0].stats_to_csv()
```