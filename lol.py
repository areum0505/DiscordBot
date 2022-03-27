# lol.py

import random
import requests


class lol:
    lanes = ['탑', '정글', '미드', '봇', '서포터']
    keystones = []
    items = []
    champions = []
    images = []
    version = ''

    def __init__(self):
        headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*'}
        # 버전
        self.version = requests.get('https://ddragon.leagueoflegends.com/api/versions.json', headers=headers).json()[0]
        # 챔피언
        champion_res = requests.get('https://ddragon.leagueoflegends.com/cdn/' + self.version + '/data/ko_KR/champion.json', headers=headers).json()['data']
        for champion in champion_res:
            self.champions.append(champion_res[champion]['name'])
            self.images.append(champion_res[champion]['image']['full'])
        # 아이템
        item_res = requests.get('https://ddragon.leagueoflegends.com/cdn/' + self.version + '/data/ko_KR/item.json', headers=headers).json()['data']
        for item in item_res:
            if 'rarityMythic' in item_res[item]['description']:
                self.items.append(item_res[item]['name'])
        # 룬
        rune_res = requests.get('https://ddragon.leagueoflegends.com/cdn/' + self.version + '/data/ko_KR/runesReforged.json', headers=headers).json()
        for i in range(len(rune_res)):
            for rune in rune_res[i]['slots'][0]['runes']:
                self.keystones.append(rune['name'])

    def getResult(self, text):
        words = text.split()

        result = {'라인': '', "룬": '', '아이템': '', '챔피언': '', '이미지': ''}

        for word in words:
            if word == "라인":
                index = random.randrange(0, len(self.lanes))
                result["라인"] = self.lanes[index]
            elif word == "룬":
                index = random.randrange(0, len(self.keystones))
                result["룬"] = self.keystones[index]
            elif word == "아이템":
                index = random.randrange(0, len(self.items))
                result["아이템"] = self.items[index]
            elif word == "챔피언":
                index = random.randrange(0, len(self.champions))
                result["챔피언"] = self.champions[index]
                result["이미지"] = 'http://ddragon.leagueoflegends.com/cdn/' + self.version + '/img/champion/' + self.images[index]

        return result
