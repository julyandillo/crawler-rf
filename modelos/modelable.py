from abc import ABCMeta, abstractmethod

from modelos.model import Model


class Modelable(metaclass=ABCMeta):
    def __init__(self, available_fields_list: list):
        self._model = Model(available_fields_list)

    def get_lista_campos_disponibles(self) -> list:
        return self._model.get_available_fields_list()

    def set(self, key: str, value: str | int | float) -> None:
        self._model.set(key, value)

    def get(self, key: str) -> int | float | str:
        return self._model.get(key)

    def get_model(self) -> dict:
        return self._model.get_modelo()

    @abstractmethod
    def json_serialize(self) -> dict:
        pass
