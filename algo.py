import sys
import base64
import numpy as np
import io
import requests
# from flask import make_response, send_file
import pandas as pd


################ check whether or not the symbol is in the markets ###############
def symbols():
    return True

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
    return playerstats