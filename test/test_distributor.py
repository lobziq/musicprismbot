import pytest
from distributor import *


@pytest.mark.parametrize('url', [
    'https://itunes.apple.com/ru/artist/the-xx/315473044',
    'https://music.yandex.ru/artist/150811',
    'https://open.spotify.com/artist/3iOvXCl6edW5Um0fXEBRXy'
])
@pytest.mark.parametrize('result', [
    ('artist', 'the xx', None)
])
def test_parse_artist(url, result):
    assert result == Distributor().parse_url(url)


@pytest.mark.parametrize('url', [
    'https://itunes.apple.com/ru/album/xx/325808192',
    'https://music.yandex.ru/album/718285',
    'https://open.spotify.com/album/0z6ErTRiEcAML2IPrkWI5W'
])
@pytest.mark.parametrize('result', [
    ('album', 'the xx', 'xx')
])
def test_parse_album(url, result):
    assert result == Distributor().parse_url(url)


@pytest.mark.parametrize('url', [
    'https://itunes.apple.com/ru/album/islands/325808192?i=325808208',
    'https://music.yandex.ru/album/718285/track/6679097',
    'https://open.spotify.com/track/2SMn57cBVxoD4TArscpovk'
])
@pytest.mark.parametrize('result', [
    ('track', 'the xx', 'islands')
])
def test_parse_song(url, result):
    assert result == Distributor().parse_url(url)
