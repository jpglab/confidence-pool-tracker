import sys
import urllib2
import re
from bs4 import BeautifulSoup

soup = BeautifulSoup(urllib2.urlopen('http://sports.yahoo.com/nfl/scoreboard/').read())

scores = soup.find_all('td', attrs={'class': 'score'})
away = soup.find_all('td', attrs={'class': 'away'})
home = soup.find_all('td', attrs={'class': 'home'})
con = {} 
away_teams = []

for a in away:
  away_teams.append(str(a.a.text))

home_teams = []
for h in home:
  home_teams.append(str(h.a.text))

scoreboard = []
for s in scores:
 scoreboard.append(str(s.a.text))

def get_scores():
  for i in range(len(scoreboard)):
    if scoreboard[i] == '@':
      print('%s [TBA] %s' %(away_teams[i], home_teams[i]))
    else:
      print('%s [%s] %s' %(away_teams[i], scoreboard[i], home_teams[i]))

def set_confidence():
  for i in range(len(scoreboard)):
    w = raw_input('Enter your winner for the %s vs. %s game: ' %(home_teams[i], away_teams[i]))
    c = raw_input('Enter your confidence for the %s vs. %s game: ' %(home_teams[i], away_teams[i]))
    con.update({'%s vs %s' %(home_teams[i], away_teams[i]) : '%s @ %s' %(w,c)})

  print con

if __name__ == '__main__':
  get_scores()
  set_confidence()
