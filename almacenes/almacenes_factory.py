from almacenes.almacenequipos import AlmacenEquipos
from almacenes.almacenequiposjson import AlmacenEquiposJson
from almacenes.almacenjornadas import AlmacenJornadas
from almacenes.almacenjornadasjson import AlmacenJornadasJson


class AlmacenesFactory:
    @staticmethod
    def get_almacen_equipos() -> AlmacenEquipos:
        return AlmacenEquiposJson()

    @staticmethod
    def get_almacen_jornadas() -> AlmacenJornadas:
        return AlmacenJornadasJson()
