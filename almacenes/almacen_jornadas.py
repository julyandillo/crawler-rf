from abc import ABCMeta, abstractmethod

from modelos.jornada import Jornada


class AlmacenJornadas(metaclass=ABCMeta):
    @abstractmethod
    def save(self, jornada: Jornada) -> None:
        pass

    @abstractmethod
    def load(self, numero_jornada: int) -> Jornada:
        pass

    @abstractmethod
    def load_all(self) -> dict:
        pass
