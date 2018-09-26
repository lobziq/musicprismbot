from bs4 import *
from urllib import parse
from handlers.handler import *
import requests
import json


class HandlerItunes(Handler):
    def __init__(self):
        super().__init__()
        self.source = 'itunes'

    def parse_url(self, url):
        try:
            item = None
            if 'artist' in url:
                itemtype = 'artist'
                artist = url.split('/')[-2].replace('-', ' ')
            else:
                r = requests.get(url, headers=self.header)
                soup = BeautifulSoup(r.text, "html.parser")
                itemtype = soup.find("meta", property="og:type")['content'].split('.')[1].replace('song', 'track')

                if itemtype in self.parseable_items:
                    artist = soup.find("meta", property="music:musician")['content'].split('/')[-2].replace('-', ' ')
                    item = url.split('/')[-2].replace('-', ' ').lower()
                else:
                    return None

            return itemtype, parse.unquote(artist), parse.unquote(item) if item else item
        except:
            return None

    def get_link(self, itemtype, artist, item):
        try:
            term = 'term=' + artist.replace(' ', '+')
            term = term + '+' + item.replace(' ', '+') if item else term
            results = json.loads(requests.get('https://itunes.apple.com/search', params=term).text)['results'][0]
            return parse.unquote(results[itemtype.replace('album', 'collection') + 'ViewUrl'])
        except:
            return None
