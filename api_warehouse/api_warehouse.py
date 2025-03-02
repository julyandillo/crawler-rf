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
            response = self._api.make_post_request('/equipos', team.prepare())
            return response['id']

        except APIError as e:
            raise WarehouseError(e) from e

    def update_team(self, id_team: int, team: Model) -> bool:
        try:
            self._api.make_patch_request(f"/equipos/{id_team}", team.prepare())
            return True

        except APIError as e:
            raise WarehouseError(str(e)) from e

    def save_player(self, player: Model) -> int:
        try:
            response = self._api.make_post_request('/jugadores', player.prepare())
            return response['id']

        except APIError as e:
            raise WarehouseError(e) from e

    def update_player(self, id_player: int, player: Model) -> None:
        try:
            self._api.make_patch_request(f"/jugadores/{id_player}", player.prepare())
        except APIError as e:
            raise WarehouseError(str(e)) from e

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

    def set_current_stadium_of_team(self, stadium: int, team: int) -> bool:
        try:
            self._api.make_post_request("/equipos/estadio", {
                'equipo': team,
                'estadio': stadium,
            })

            return True

        except APIError as e:
            raise WarehouseError(str(e)) from e

    def save_squad(self, players: list[dict]) -> int:
        try:
            response = self._api.make_post_request('/plantillas', {
                'jugadores': players
            })

            return response['plantilla']

        except APIError as e:
            raise WarehouseError(str(e)) from e

    def associate_team_squad_competition(self, team_id: int, squa_id: int, competition_id: int) -> None:
        try:
            self._api.make_post_request(f"/equipos/{team_id}/competiciones", {
                'competicion': competition_id,
                'plantilla': squa_id
            })

        except APIError as e:
            raise WarehouseError(f"{e}") from e
