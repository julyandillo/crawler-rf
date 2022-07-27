import json

from almacenes.almacen import Almacen

EQUIPOS_JSON = 'equipos.json'


class AlmacenEquipos(Almacen):

    def __init__(self):
        self._equipos_almacenados = {}

    def guarda(self, equipos: list):
        with open(EQUIPOS_JSON, 'w') as fichero:
            json.dump([equipo.get_modelo() for equipo in equipos], fichero)

    def lee(self, clave: int | str):
        if not self._equipos_almacenados:
            """ los diccionarios vacios se evaluan como False"""
            with open(EQUIPOS_JSON, 'r') as fichero:
                for equipo in json.load(fichero):
                    self._equipos_almacenados[equipo.get('Nombre corto')] = equipo

        return self._equipos_almacenados.get(clave, 'Equipo no encontrado')
