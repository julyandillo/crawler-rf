from datetime import datetime

from modelos.modelable import Modelable
from modelos.json_structure import JsonStructure
from utils.utils import date_time_format


class Partido(Modelable):
    contador = 0

    modelo = [
        'id',
        'equipo_local',
        'equipo_visitante',
        'fecha'
    ]

    def __init__(self):
        super().__init__(Partido.modelo)
        self.__class__.contador += 1

        self.set('id', self.contador)
        self.equipo_local = ''
        self.equipo_visitante = ''
        self.fecha: datetime = datetime.now()

    def __str__(self):
        return f'[{str(self.id).zfill(3)}] | {self.equipo_local.center(15)} - {self.equipo_visitante.center(15)} ' \
               f'[{self.get_fecha()} {self.get_hora()}]'

    def set_equipo_local(self, nombre_equipo: str):
        self.equipo_local = nombre_equipo
        self.set('equipo_local', nombre_equipo)

    def set_equipo_visitante(self, nombre_equipo: str):
        self.equipo_visitante = nombre_equipo
        self.set('equipo_visitante', nombre_equipo)

    def set_fecha(self, fecha: datetime):
        self.fecha = fecha
        self.set('fecha', date_time_format(fecha))

    def get_fecha(self) -> str:
        return self.fecha.strftime('%d-%m-%Y')

    def get_hora(self) -> str:
        return self.fecha.strftime('%H:%M')

    @classmethod
    def get_json_structure(cls) -> JsonStructure:
        return JsonStructure(
            'id',
            Partido.modelo
        )
