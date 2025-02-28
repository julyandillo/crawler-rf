import requests
from bs4 import BeautifulSoup

from exceptions.crawler_error import CrawlerError


def get_content_url(url) -> str:
    response = requests.get(url)

    if response.status_code != requests.codes.ok:
        raise CrawlerError(f"Ha ocurrido un error al realizar la petición.\n{url} - {response.status_code}")

    response.encoding = 'utf-8'
    return response.text


class Sopa:
    def __init__(self, url: str):
        self._url = url

    def get_sopa(self) -> BeautifulSoup | None:
        try:
            return BeautifulSoup(get_content_url(self._url), 'lxml')

        except CrawlerError as e:
            print(e)
