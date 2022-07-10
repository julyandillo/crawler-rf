from modelos.modelo import Modelo


class Estadio(Modelo):
    def __init__(self):
        super().__init__([
            'Nombre del estadio',
            'Capacidad',
            'Dirección',
            'Año de construcción',
            'Tamaño',
            'Ciudad'
        ])

    def __str__(self):
        return f"{self.get_nombre()} [{self.get_capacidad()} espectadores], {self.get('Ciudad')}"

    def get_nombre(self) -> str:
        return self.get('Nombre del estadio').replace('Estadio ', '')

    def get_capacidad(self) -> int:
        return int(self.get('Capacidad'))

    def set_ciudad(self, ciudad: str):
        self.guarda('Ciudad', ciudad)

