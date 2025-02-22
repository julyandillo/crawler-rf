from warehouse.model import Model
from warehouse.warehouse import Warehouse
from warehouse.warehouse_error import WarehouseError
from .api import API
from .api_error import APIError


class APIWarehouse(Warehouse):
    """ Clase para controlar las peticiones que se realizan a la API """

    def __init__(self):
        self._api = API()

    def save_team(self, team: Model) -> int:
        try:
            entity = team.prepare()
            response = self._api.make_post_request('/equipos', entity)

            return response['id']

        except APIError as e:
            raise WarehouseError(e) from e

    def update_team(self, id_team: int, team: Model) -> bool:
        try:
            entity = team.prepare()
            self._api.make_patch_request(f"/equipos/{id_team}", entity)

            return True

        except APIError as e:
            raise WarehouseError(str(e)) from e

    def save_player(self, player: Model) -> int:
        entity = player.prepare()
        response = self._api.make_post_request('/jugadores', entity)

        return response['id']

    def save_stadium(self, stadium: Model) -> int:
        try:
            response = self._api.make_post_request('/estadios', stadium.prepare())
            return response['id']

        except APIError as e:
            raise WarehouseError(str(e)) from e

    def update_stadium(self, id_stadium: int, stadium: Model) -> bool:
        try:
            self._api.make_patch_request(f"/estadio/{id_stadium}", stadium.prepare())

            return True

        except APIError as e:
            raise WarehouseError(str(e)) from e

    def set_stadium_for_team(self, stadium: int, team: int) -> bool:
        try:
            self._api.make_post_request("/equipos/estadio", {
                'equipo': team,
                'estadio': stadium,
            })

            return True

        except APIError as e:
            raise WarehouseError(str(e)) from e
