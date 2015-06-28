import json
import requests


def playerID(first_last):
	#search common player all
	url = "http://stats.nba.com/stats/commonallplayers?LeagueID=00&Season=2015-16&IsOnlyCurrentSeason=1"
	response = requests.get(url)

	#get player id
	active = response.json()['resultSets'][0]['rowSet']
	for player in active:
		if (player[5] == first_last):
			#player id
			return player[0]


def playerStats(first_last):
	# get player's id
	pID = str(playerID(first_last))
	if(pID == 0 or pID == None):
		return "Player not found."

	# common player info
	url = "http://stats.nba.com/stats/commonplayerinfo?PlayerId="+pID
	response = requests.get(url)

	player = response.json()['resultSets'][0]['rowSet']
	name = player[0][3];
	player = response.json()['resultSets'][1]['rowSet']
	pts = str(player[0][3])
	ast = str(player[0][4])
	reb = str(player[0][5])
	pie = str(player[0][6])
	return 	"AVG Stats for "+name+": PTS= "+pts+", AST= "+ast+", REB= "+reb+", PIE= "+pie