from modelos.json_structure import JsonStructure
from modelos.modelable import Modelable


class Estadio(Modelable):
    def __init__(self):
        super().__init__([
            'Nombre del estadio',
            'Capacidad',
            'Dirección',
            'Año de construcción',
            'Tamaño',
            'Ciudad',
        ])

    def __str__(self):
        return f"{self.get_nombre()} [{self.get_capacidad()} espectadores], {super().get('Ciudad')}"

    def get_nombre(self) -> str:
        return super().get('Nombre del estadio').replace('Estadio ', '')

    def get_capacidad(self) -> int:
        return int(super().get('Capacidad'))

    def set_ciudad(self, ciudad: str):
        super().set('Ciudad', ciudad)

    @classmethod
    def get_json_structure(cls) -> JsonStructure:
        return JsonStructure('Nombre del estadio', super().get_model().keys())
