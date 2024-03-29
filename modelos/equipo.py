from modelos.json_structure import JsonStructure
from modelos.modelable import Modelable


class Equipo(Modelable):
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
            'Ciudad',
            'Pais',
        ])

        super().set('Pais', 'España')

    def __str__(self):
        return f"{super().get('Nombre del equipo')} ({super().get('Nombre corto')})"

    def get_ciudad(self) -> str:
        return super().get('Ciudad')

    @classmethod
    def get_json_structure(cls) -> JsonStructure:
        return JsonStructure(
            'Nombre corto',
            [
                'Nombre corto',
                'Nombre completo',
                'Nombre del equipo',
                'Presidente',
                'Ciudad',
                'Sitio Web',
                'Entrenador',
                'Año de Fundación',
                'Pais'
            ])
