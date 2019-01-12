import requests

URL = "ADD YOUR URL HERE"

headers = {
	'TRN-Api-Key' : 'ADD YOUR TRN API KEY HERE'
}

def get_player_stats(playername):
	playerurl = "https://api.fortnitetracker.com/v1/profile/pc/" + playername
	playerresponse = requests.get(playerurl, headers = headers)
	playerinfo = playerresponse.json()['lifeTimeStats']
	#playerstats = list: matches played, wins, win%, kills, k/d
	playerstats = [int(playerinfo[7]['value']), int(playerinfo[8]['value']), int(playerinfo[9]['value'][:-1]), int(playerinfo[10]['value']), float(playerinfo[11]['value'])]

	
	#recents = list of K/D ratio through last 10 sessions
	recents = []
	for i in playerresponse.json()['recentMatches']:
		kd = i['kills'] / i['matches']
		recents.append(round(kd, 2))

	for i in range(len(recents), 10):
		recents.append(0)

	#wins: [solos, duos, squads]
	stats = playerresponse.json()['stats']
	wins = [stats['p2']['top1']['value'], stats['p10']['top1']['value'], stats['p9']['top1']['value']]

	return playerstats, recents, wins
