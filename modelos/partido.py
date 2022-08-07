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

    reemplazos = {
        'Sociedad': 'Real Sociedad',
        'Real': 'Valladolid'
    }

    def __init__(self):
        super().__init__(Partido.modelo)
        self.__class__.contador += 1

        self.set('id', self.contador)
        self.equipo_local = ''
        self.equipo_visitante = ''
        self.fecha: datetime = datetime.now()

    def __repr__(self):
        return f'[{str(self.get("id").zfill(3))}] | {self.equipo_local.center(15)} - {self.equipo_visitante.center(15)} ' \
               f'[{self.get_fecha()} {self.get_hora()}]'

    def set_equipo_local(self, nombre_equipo: str):
        self.equipo_local = nombre_equipo if nombre_equipo not in self.__class__.reemplazos.keys() else \
            self.__class__.reemplazos.get(nombre_equipo)
        self.set('equipo_local', self.equipo_local)

    def set_equipo_visitante(self, nombre_equipo: str):
        self.equipo_visitante = nombre_equipo if nombre_equipo not in self.__class__.reemplazos.keys() else \
            self.__class__.reemplazos.get(nombre_equipo)
        self.set('equipo_visitante', self.equipo_visitante)

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
