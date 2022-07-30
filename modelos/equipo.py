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
        ])

    def __str__(self):
        return f"{super().get('Nombre del equipo')} ({super().get('Nombre corto')})"

    def get_ciudad(self) -> str:
        return super().get('Ciudad')

    def get_fields_to_json_serialize(self) -> list:
        return [
            'Nombre corto',
            'Nombre completo',
            'Ciudad',
        ]
