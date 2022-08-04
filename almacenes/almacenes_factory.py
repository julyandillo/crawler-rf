from almacenes.almacenequipos import AlmacenEquipos
from almacenes.almacenequiposjson import AlmacenEquiposJson


class AlmacenesFactory:
    @classmethod
    def get_almacen_equipos(cls) -> AlmacenEquipos:
        return AlmacenEquiposJson()
