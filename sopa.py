import requests

from bs4 import BeautifulSoup


class Sopa:
    def __init__(self, url: str):
        self._url = url
        self._response = None

    def get_sopa(self) -> BeautifulSoup:
        self.realiza_peticion()
        return BeautifulSoup(self._response.text, 'lxml')

    def realiza_peticion(self):
        self._response = requests.get(self._url)
        self._response.encoding = 'utf-8'
