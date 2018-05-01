from fake_useragent import UserAgent


class Handler:
    def __init__(self):
        self.source = None
        self.header = {'User-Agent': str(UserAgent().chrome)}
        self.parseable_items = ['artist', 'album', 'track']

    def parse_url(self, url):
        raise NotImplementedError

    def get_link(self, itemtype, artist, item):
        raise NotImplementedError
