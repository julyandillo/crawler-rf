from abc import ABCMeta, abstractmethod

from modelos.model import Model
from modelos.json_structure import JsonStructure


class Modelable(metaclass=ABCMeta):
    def __init__(self, available_fields_list: list):
        self._model = Model(available_fields_list)

    def get_lista_campos_disponibles(self) -> list:
        return self._model.get_available_fields_list()

    def set(self, key: str, value: str | int | float | list) -> None:
        self._model.set(key, value)

    def get(self, key: str) -> int | float | str:
        return self._model.get(key)

    def get_model(self) -> dict:
        return self._model.get_modelo()

    def json_serialize(self) -> dict:
        """
        para poder guardar cada modelo como json, se devuelve un diccionario SOLO con los valores que están
        definidos para ser almacenados en cada modelo
        """
        return {key: value for key, value in self._model.get_modelo().items() if
                key in self.get_json_structure().values}

    @classmethod
    @abstractmethod
    def get_json_structure(cls) -> JsonStructure:
        pass
