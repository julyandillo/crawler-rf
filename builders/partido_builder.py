from datetime import datetime


from modelos.partido import Partido


class PartidoBuilder:

    def __init__(self, data: dict):
        self._partido = Partido()

        self._partido.set('id', data.get('id'))
        self._partido.set_equipo_local(data.get('equipo_local'))
        self._partido.set_equipo_visitante(data.get('equipo_visitante'))
        self._partido.set_fecha(datetime.strptime(data.get('fecha'), '%d-%m-%Y %H:%M:%S'))

    def get_partido(self) -> Partido:
        return self._partido
