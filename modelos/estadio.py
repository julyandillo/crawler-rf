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

    def json_serialize(self) -> dict:
        return super().get_model()

