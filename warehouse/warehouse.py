from abc import ABCMeta, abstractmethod

from .model import Model
from .warehouse_error import WarehouseError


class Warehouse(metaclass=ABCMeta):
    def save_model(self, model: Model) -> int:
        methods_by_model_type = {
            Model.TEAM_TYPE: self.save_team,
            Model.STADIUM_TYPE: self.save_stadium,
            Model.PLAYER_TYPE: self.save_player,
        }

        if model.get_type() not in methods_by_model_type:
            raise WarehouseError('No se puede guardar el modelo, tipo no encontrado')

        return methods_by_model_type[model.get_type()](model)

    def update_model(self, id_entity: int, model: Model) -> bool:
        methods_by_model_type = {
            Model.TEAM_TYPE: self.update_team,
            Model.STADIUM_TYPE: self.update_stadium,
            Model.PLAYER_TYPE: self.update_player,
        }

        if model.get_type() not in methods_by_model_type.keys():
            raise WarehouseError('No se puede actualizar el modelo, tipo no encontrado')

        return methods_by_model_type[model.get_type()](id_entity, model)

    @abstractmethod
    def save_team(self, team: Model) -> int:
        pass

    @abstractmethod
    def update_team(self, id_entity: int, team: Model) -> bool:
        pass

    @abstractmethod
    def save_player(self, player: Model) -> int:
        pass

    @abstractmethod
    def update_player(self, id_entity: int, player: Model) -> bool:
        pass

    @abstractmethod
    def save_stadium(self, stadium: Model) -> int:
        pass

    @abstractmethod
    def update_stadium(self, id_entity: int, stadium: Model) -> bool:
        pass

    @abstractmethod
    def set_current_stadium_of_team(self, stadium: int, team: int) -> bool:
        pass

    @abstractmethod
    def save_squad(self, players: list[dict]) -> int:
        pass

    @abstractmethod
    def associate_team_squad_competition(self, team_id: int, squa_id: int, competition_id: int) -> None:
        pass
