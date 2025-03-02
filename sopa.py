import requests
from bs4 import BeautifulSoup

from exceptions.crawler_error import CrawlerError


class Sopa:
    def __init__(self, url: str):
        self._url = url

    def get_sopa(self) -> BeautifulSoup | None:
        response = requests.get(self._url)

        if response.status_code != requests.codes.ok:
            raise CrawlerError(
                f"Ha ocurrido un error al realizar la petición, url:{self._url} - {response.status_code}")

        response.encoding = 'utf-8'

        return BeautifulSoup(response.text, 'lxml')
