import json

from modelos.equipo import Equipo
from services.jsonservices import json_serializer

FILE_TEAMS = 'equipos.json'


class AlmacenEquipos:
    def __init__(self):
        self._equipos_almacenados = {}

    def save_all_teams(self, equipos: list[Equipo]):
        json_serializer(FILE_TEAMS, equipos)

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
        with open(FILE_TEAMS, 'r') as fichero:
            for equipo in json.load(fichero):
                self._equipos_almacenados[equipo.get('Nombre corto')] = equipo
