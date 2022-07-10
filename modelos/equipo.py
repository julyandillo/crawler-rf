from modelos.modelo import Modelo


class Equipo(Modelo):
    def __init__(self):
        super().__init__([
            'Nombre corto',
            'Nombre completo',
            'Nombre del equipo',
            'Entrenador',
            'Presidente',
            'URL del equipo en RF',
            'Año de Fundación',
            'Sitio Web',
            'Ciudad'
        ])

    def __str__(self):
        return f"{self.get('Nombre del equipo')} ({self.get('Nombre corto')})"

    def get_ciudad(self) -> str:
        return self.get('Ciudad')
