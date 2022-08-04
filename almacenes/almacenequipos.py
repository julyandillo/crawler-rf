from abc import ABCMeta, abstractmethod

from modelos.equipo import Equipo


class AlmacenEquipos(metaclass=ABCMeta):
    @abstractmethod
    def save_all_teams(self, teams: list[Equipo]) -> None:
        pass

    @abstractmethod
    def save_team(self, team: Equipo) -> None:
        pass

    def load_team(self, key: int | str) -> Equipo:
        pass

    @abstractmethod
    def load_all_teams(self) -> None:
        pass
