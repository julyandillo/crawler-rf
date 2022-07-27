import json

from almacenes.almacen import Almacen

EQUIPOS_JSON = 'equipos.json'


class AlmacenEquipos(Almacen):
    def guarda(self, equipos: list):
        with open(EQUIPOS_JSON, 'w') as fichero:
            json.dump([equipo.get_modelo() for equipo in equipos], fichero)

    def lee(self, clave: int | str):
        with open(EQUIPOS_JSON, 'r') as fichero:
            equipos = json.load(fichero)

            return equipos.get(clave, 'Equipo no encontrado')
