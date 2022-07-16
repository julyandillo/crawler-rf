from dataclasses import dataclass
from datetime import datetime


@dataclass
class Partido:
    equipo_local: str = ''
    equipo_visitante: str = ''
    fecha: datetime = datetime.now()

    def __str__(self):
        return f'{self.equipo_local.center(15)} - {self.equipo_visitante.center(15)} [{self.get_fecha()} {self.get_hora()}]'

    def get_fecha(self) -> str:
        return self.fecha.strftime('%d-%m-%Y')

    def get_hora(self) -> str:
        return self.fecha.strftime('%H:%M')
