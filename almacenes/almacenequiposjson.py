from almacenes.almacenequipos import AlmacenEquipos
from modelos.equipo import Equipo
from utils.utils import generate_dict_from_list
from services.jsonservices import save_as_json, load_from_json

FILE_TEAMS = 'equipos.json'


class AlmacenEquiposJson(AlmacenEquipos):
    def __init__(self):
        self._equipos_almacenados = {}

    def save_all_teams(self, teams: list[Equipo]) -> None:
        save_as_json(FILE_TEAMS, teams)
        self._equipos_almacenados = generate_dict_from_list(Equipo.get_json_structure().key, teams)

    def save_team(self, equipo: Equipo) -> None:
        if not self._equipos_almacenados:
            self.load_all_teams()

        # se añade el nuevo equipo al diccionario (si ya existía se reeemplazará por el nuevo)
        self._equipos_almacenados[Equipo.get_json_structure().key] = equipo

        self.save_all_teams(list(self._equipos_almacenados.values()))

    def load_team(self, clave: int | str) -> Equipo:
        if not self._equipos_almacenados:
            """ los diccionarios vacios se evaluan como False """
            self.load_all_teams()

        return self._equipos_almacenados.get(clave, 'Equipo no encontrado')

    def load_all_teams(self) -> None:
        self._equipos_almacenados = generate_dict_from_list(Equipo.get_json_structure().key,
                                                            load_from_json(FILE_TEAMS))
