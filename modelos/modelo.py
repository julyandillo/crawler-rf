class Modelo:

    def __init__(self, datos_necesarios: list):
        self._datos_necesarios = datos_necesarios
        self._modelo = {}

    def get_lista_datos_necesarios(self) -> list:
        return self._datos_necesarios

    def guarda(self, key: str, valor: str | int | float):
        if key not in self._datos_necesarios:
            raise ValueError(key)

        self._modelo[key] = valor

    def get(self, key: str) -> str | int | float:
        if key not in self._modelo.keys():
            """ 
            se comprueba si está en las keys de la información rastreada por que es posible que esté en la lista
            de los datos necesarios pero no se haya podido rastrear, con lo que no estará en el diccionario
            """
            return 'Información no rastreada'

        return self._modelo.get(key)

    def get_modelo(self) -> dict:
        return self._modelo
