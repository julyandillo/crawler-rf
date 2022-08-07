from datetime import datetime

from modelos.json_structure import JsonStructure
from modelos.modelable import Modelable
from modelos.partido import Partido
from utils.utils import date_format


class Jornada(Modelable):
    modelo = [
        'numero',
        'fecha_inicio',
        'fecha_fin',
        'partidos'
    ]

    def __init__(self):
        super().__init__(Jornada.modelo)

        self._time_fecha_inicio = None
        self._time_fecha_fin = None
        self._partidos = []

    def __str__(self):
        return f"Jornada {self.get('numero')}"

    def set_numero(self, numero: int) -> None:
        self.set('numero', numero)

    def get_numero(self) -> int:
        return self.get('numero')

    def agrega_partido(self, partido: Partido):
        self._partidos.append({key: partido.get(key) for key in Partido.get_json_structure().values})
        self.establece_fechas_de_jornada(partido.get_fecha())
        self.set('partidos', self._partidos)

    def establece_fechas_de_jornada(self, fecha: str):
        fecha_nueva = datetime.strptime(fecha, '%d-%m-%Y')

        if not self._time_fecha_inicio or self._time_fecha_inicio > fecha_nueva:
            self._time_fecha_inicio = fecha_nueva

        if not self._time_fecha_fin or self._time_fecha_fin < fecha_nueva:
            self._time_fecha_fin = fecha_nueva

        self.set('fecha_inicio', date_format(self._time_fecha_inicio))
        self.set('fecha_fin', date_format(self._time_fecha_fin))

    def ver_jornada(self):
        print("".ljust(50, "-"))
        print(f'Jornada {self.get("numero")}:')
        print(f"Inicio: {self.get('fecha_inicio')} | Fin: {self.get('fecha_fin')}")
        print(''.ljust(50, '-'))
        print(*self._partidos, sep='\n')

    @staticmethod
    def crea_jornada(jornada_almacenada: dict):
        jornada = Jornada()
        for key, value in jornada_almacenada.items():
            if key != 'partidos':
                jornada.set(key, value)
            else:
                for partido_almacenado in value:
                    jornada.agrega_partido(Partido.crea_partido(partido_almacenado))

        return jornada

    @classmethod
    def get_json_structure(cls) -> JsonStructure:
        return JsonStructure(
            'numero',
            Jornada.modelo
        )
