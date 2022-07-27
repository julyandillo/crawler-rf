from abc import ABCMeta, abstractmethod


class Almacen(metaclass=ABCMeta):
    @abstractmethod
    def guarda(self, datos: dict | list):
        pass

    @abstractmethod
    def lee(self, clave: int | str):
        pass
