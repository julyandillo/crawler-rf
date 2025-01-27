import json
import os
import time

import requests

from .api_error import APIError

URL = 'http://localhost:8000/api'


class API:
    __location = os.path.abspath(os.path.dirname(__file__))

    def __init__(self):
        self._load_token()

        self._headers = {
            'Authorization': f"Bearer {self._token}"
        }
        self._content = {}

    def _load_token(self):
        with open(os.path.join(self.__location, 'token.json'), 'r') as file:
            filecontent = json.load(file)

            if time.localtime() > time.strptime(filecontent['expire'], '%Y-%m-%d %H:%M:%S'):
                raise APIError('Token expired. Please, obtain a new valid token')

            self._token = filecontent['token']

    def make_post_request(self, path: str, entity: dict) -> dict:
        # con el parámetro json se añade automáticamente la cabecera Content-type: application/json
        response = requests.post(f"{URL}{path}", headers=self._headers, json=entity)
        self._parse_response(response)

        return self._content

    def _parse_response(self, response: requests.Response) -> None:
        self._content = response.json()

        if response.status_code == requests.codes.unauthorized:
            raise APIError(self._content['message'])

        if response.status_code != requests.codes.ok:
            raise APIError(f"{self._content['msg']} {self._content['detalles'] or ''}")

    def make_patch_request(self, path: str, entity: dict) -> dict:
        response = requests.patch(f"{URL}{path}", headers=self._headers, json=entity)
        self._parse_response(response)

        return self._content

    def make_get_request(self, path: str, params: dict) -> dict:
        response = requests.get(f"{URL}{path}", params=params, headers=self._headers)
        self._parse_response(response)

        return self._content
