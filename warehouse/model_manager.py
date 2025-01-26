from abc import ABCMeta, abstractmethod

from .model import Model


class ModelManager(metaclass=ABCMeta):
    @abstractmethod
    def get_team_model(self) -> Model:
        pass

    @abstractmethod
    def get_stadium_model(self) -> Model:
        pass

    @abstractmethod
    def get_player_model(self) -> Model:
        pass
