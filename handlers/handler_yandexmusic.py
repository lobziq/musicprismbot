from bs4 import *
from handlers.handler import *
import requests


class HandlerYandexmusic(Handler):
    def __init__(self):
        super().__init__()
        self.source = 'yandex'

    def parse_url(self, url):
        try:
            r = requests.get(url, headers=self.header)
            soup = BeautifulSoup(r.text, "html.parser")
            itemtype = url.split('/')[-2]

            if itemtype in self.parseable_items:
                if itemtype == 'artist':
                    artist = soup.find(class_='page-artist__title').text.lower()
                    return itemtype, artist, None
                artist = soup.select_one("a[href*=/artist/]").text.lower()
                if itemtype == 'track':
                    tail = url.split('music.yandex.ru/')[-1]
                    item = soup.select_one("a[href*={0}]".format(tail)).text.lower()
                if itemtype == 'album':
                    item = soup.find(class_='page-album__title').text.lower()
            else:
                return None

            return itemtype, artist, item
        except:
            return None

    def get_link(self, itemtype, artist, item):
        try:
            s = 'https://music.yandex.ru/search?text={0}'.format(artist.replace(' ', '+'))
            s = s + '+' + item.replace(' ', "+") if item else s
            return s
        except:
            return None