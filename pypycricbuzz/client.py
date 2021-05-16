import requests
import hmac
import time
from hashlib import sha1
from typing import List
from .models.match import Match


class CricbuzzClient:

    def __init__(self, session=requests.session()) -> None:
        super().__init__()
        self.s = session
        self.s.headers = {"authentication": self.__hmac_generate(),
                          "cb-tz": "+0530",
                          "cb-src": "playstore",
                          "cb-appver": "5.01.04",
                          "cb-loc": "IN",
                          "Accept": "application/json"
                          }
        self.base_url = "https://api.cricbuzz.com/a"

    def __regen_hmac(self) -> None:
        self.s.headers['authentication'] = self.__hmac_generate()

    @staticmethod
    def __hmac_generate() -> str:
        secret_key = bytes.fromhex("53b14cafa7c9a22cd6f2d04e82f174e4e3ffcc51e324920dab98c96ca288e67c")
        t = round(time.time()) + 300  # valid for 5 minute (simulating official cricbuzz app client)
        raw = f'exp={t}~acl=/*'
        h = hmac.new(secret_key, raw.encode(), sha1)
        hmac_hash = h.digest().hex()
        return f'{raw}~hmac={hmac_hash}'

    def get_featured_matches(self) -> List[Match]:
        """
        fetches featured matches from the cricbuzz api
        :return: list of matches: list[Match]
        """
        res = self.s.get(f'{self.base_url}/home/v1/index')
        data = res.json()
        r = []
        for i in data['matches']:
            r.append(Match(i))
        return r

    def get_series_matches(self, seriesId: int) -> List[Match]:
        """
        fetches matches in a series from the cricbuzz api
        :param seriesId: Cricbuzz id of the series
        :return: list of matches in the series
        """
        res = self.s.get(f'{self.base_url}/series/v1/{seriesId}')
        data = res.json()
        r = []
        for i in data['matchDetails']:
            for match in i['match']:
                r.append(Match(match))
        return r
