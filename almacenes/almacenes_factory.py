from almacenes.almacen_equipos import AlmacenEquipos
from almacenes.almacen_equipos_json import AlmacenEquiposJson
from almacenes.almacen_jornadas import AlmacenJornadas
from almacenes.almacen_jornadas_json import AlmacenJornadasJson


class AlmacenesFactory:
    @staticmethod
    def get_almacen_equipos() -> AlmacenEquipos:
        return AlmacenEquiposJson()

    @staticmethod
    def get_almacen_jornadas() -> AlmacenJornadas:
        return AlmacenJornadasJson()
