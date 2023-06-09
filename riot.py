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

    def get_match_list_data(self):
        puuid = self.get_puuid
        print(puuid)

        # the problem lies with getting the puuid into the api_url
        api_url = 'https://' + 'americas' + '.api.riotgames.com/lol/match/v5/matches/by-puuid/' + puuid + '&api_key=' + self.api_key
        match_list_data = requests.get(api_url)    
        print(match_list_data)
        match_list_data = match_list_data.json()
        return match_list_data
    
    def did_win(puuid, match_list_data):
        part_index = match_list_data['metadata']['participants'].index(puuid)
        return match_list_data['info']['participants'][part_index]['win']