from datetime import datetime

from modelos.jsonstructure import JsonStructure
from modelos.modelable import Modelable
from modelos.partido import Partido
from utils.utils import date_format


class Jornada(Modelable):
    def __init__(self, numero: int):
        super().__init__([
            'numero',
            'fecha_inicio',
            'fecha_fin'
        ])

        self.numero = numero
        self.fecha_inicio = None
        self.fecha_fin = None
        self._partidos = []

    def __str__(self):
        return f'Jornada {self.numero}'

    def agrega_partido(self, partido: Partido):
        self._partidos.append(partido)
        fecha_partido = datetime.strptime(partido.get_fecha(), '%d-%m-%Y')

        if not self.fecha_inicio or self.fecha_inicio > fecha_partido:
            self.fecha_inicio = fecha_partido

        if not self.fecha_fin or self.fecha_fin < fecha_partido:
            self.fecha_fin = fecha_partido

        super().set('fecha_inicio', date_format(self.fecha_inicio))
        super().set('fecha_fin', date_format(self.fecha_fin))

    def ver_jornada(self):
        print(''.ljust(50, '-'))
        print(f'Jornada {self.numero}:')
        print(f"Inicio: {date_format(self.fecha_inicio)} | Fin: {date_format(self.fecha_fin)}")
        print(''.ljust(50, '-'))
        print(*self._partidos, sep='\n')

    @classmethod
    def get_json_structure(cls) -> JsonStructure:
        return JsonStructure(
            'numero',
            super().get_model().keys()
        )
