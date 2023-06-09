import requests
import config

class Riot():
    def __init__(self, region, summoner):
        self.region = region
        self.summoner = summoner
        self.api_key = config.riotapi

    def get_puuid(self):
        api_url = 'https://' + self.region + '.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + self.summoner + '?api_key=' + self.api_key
        resp = requests.get(api_url)
        player_info = resp.json()
        puuid = player_info['puuid']
        return puuid

    def get_match_data(self):
        api_url = 'https://' + self.region + '.api.riotgames.com/lol/match/v5/matches/by-puuid/' + self.get_puuid() + '?api_key=' + self.api_key
        match_data = requests.get(api_url)
        match_data = match_data.json()
        print(match_data)
        return match_data
    
    def did_win(puuid, match_data):
        part_index = match_data['metadata']['participants'].index(puuid)
        return match_data['info']['participants'][part_index]['win']