import json

from modelos.equipo import Equipo
from services.jsonservices import json_serialize, json_deserialize

FILE_TEAMS = 'equipos.json'


def _dict_generate_from_list(teams):
    return {team.get('Nombre corto'): team for team in teams}


class AlmacenEquipos:
    def __init__(self):
        self._equipos_almacenados = {}

    def save_all_teams(self, teams: list[Equipo]):
        json_serialize(FILE_TEAMS, teams)
        self._equipos_almacenados = _dict_generate_from_list(teams)

    def save_team(self, equipo: Equipo):
        if not self._equipos_almacenados:
            self.load_all_teams()

        # se añade el nuevo equipo al diccionario (si ya existía se reeemplazará por el nuevo)
        self._equipos_almacenados['Nombre corto'] = equipo

        self.save_all_teams(list(self._equipos_almacenados.values()))

    def load_team(self, clave: int | str):
        if not self._equipos_almacenados:
            """ los diccionarios vacios se evaluan como False """
            self.load_all_teams()

        return self._equipos_almacenados.get(clave, 'Equipo no encontrado')

    def load_all_teams(self):
        self._equipos_almacenados = _dict_generate_from_list(json_deserialize(FILE_TEAMS))
