from modelos.jornada import Jornada
from builders.partido_builder import PartidoBuilder


class JornadaBuilder:

    def __init__(self, data: dict):
        self._jornada = Jornada()

        self._jornada.set_numero(data.get('numero'))
        for partido_almacenado in data.get('partidos'):
            self._jornada.agrega_partido(PartidoBuilder(partido_almacenado).get_partido())

    def get_jornada(self) -> Jornada:
        return self._jornada
