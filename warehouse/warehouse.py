from abc import ABCMeta, abstractmethod

from .model import Model


class Warehouse(metaclass=ABCMeta):
    @abstractmethod
    def save_team(self, team: Model) -> int:
        pass

    @abstractmethod
    def update_team(self, id_team: int, team: Model) -> bool:
        pass

    @abstractmethod
    def save_player(self, player: Model) -> int:
        pass

    @abstractmethod
    def save_stadium(self, stadium: Model) -> int:
        pass

    @abstractmethod
    def update_stadium(self, id_stadium: int, stadium: Model) -> bool:
        pass

    @abstractmethod
    def set_stadium_for_team(self, stadium: int, team: int) -> bool:
        pass
