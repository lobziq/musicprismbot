from musicprism.handlers.handler_itunes import *
from musicprism.handlers.handler_yandexmusic import *
from musicprism.handlers.handler_spotify import *


class Distributor:
    def __init__(self):
        self.handlers = []
        self.handlers.append(HandlerItunes())
        self.handlers.append(HandlerYandexmusic())
        self.handlers.append(HandlerSpotify())

    def parse_url(self, url):
        for h in self.handlers:
            if h.source in url:
                return h.parse_url(url)

        return None

    def result_to_string(self, itemtype, artist, item):
        return '{0}: {1} - {2}'.format(itemtype, artist, item) if item else '{0}: {1}'.format(itemtype, artist)

    def get_results(self, url):
        itemtype, artist, item = self.parse_url(url)
        title = self.result_to_string(itemtype, artist, item)
        results = list()

        for h in self.handlers:
            if h.source not in url:
                link = h.get_link(itemtype, artist, item)
                results.append((h.source,
                                link if link else 'can\'t find enything :C'))

        return title, results
