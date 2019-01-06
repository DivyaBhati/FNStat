#TRN-Api-Key: 805daa19-876e-4b8a-b352-0f9d499c1391
import requests

URL = "https://api.fortnitetracker.com/v1/profile/pc/divzzz"

headers = {
	'TRN-Api-Key' : '805daa19-876e-4b8a-b352-0f9d499c1391'
}

def get_player_stats(playername):
	playerurl = "https://api.fortnitetracker.com/v1/profile/pc/" + playername
	playerresponse = requests.get(playerurl, headers = headers)
	playerinfo = playerresponse.json()['lifeTimeStats']
	#playerstats = list: matches played, wins, win%, kills, k/d
	playerstats = []
	for i in range(7,12):
		playerstats.append(playerinfo[i]['value'])
	
	#recents = list of K/D ratio through last 10 sessions
	recents = []
	for i in playerresponse.json()['recentMatches']:
		kd = i['kills'] / i['matches']
		recents.append(round(kd, 2))

	#wins: [solos, duos, squads]
	stats = playerresponse.json()['stats']
	wins = [stats['p2']['top1']['value'], stats['p10']['top1']['value'], stats['p9']['top1']['value']]

	return playerstats, recents, wins