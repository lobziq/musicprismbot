from spotipy.oauth2 import SpotifyClientCredentials
from config import *
from handlers.handler import *

import spotipy


class HandlerSpotify(Handler):
    def __init__(self):
        super().__init__()
        self.source = 'spotify'
        self.client_credentials_manager = SpotifyClientCredentials(config.get('spotify_clientid'), config.get('spotify_clientsecret'))
        self.spotify = spotipy.Spotify(client_credentials_manager=self.client_credentials_manager)

    def parse_url(self, url):
        try:
            id = url.split('/')[-1]
            itemtype = url.split('/')[-2]

            if itemtype in self.parseable_items:
                data = getattr(self.spotify, itemtype)(id)
                if itemtype == 'artist':
                    return itemtype, data['name'].lower(), None
                else:
                    return itemtype, data['artists'][0]['name'].lower(), data['name'].lower()
        except:
            return None

    def get_link(self, itemtype, artist, item):
        try:
            q = artist.replace('+', '_') + ' ' + item.replace('+', '_') if item else artist
            data = self.spotify.search(q, type=itemtype)
            return data[itemtype + 's']['items'][0]['external_urls']['spotify']
        except:
            return None