import os

from dotenv import load_dotenv

from api_warehouse.api_model_manager import APIModelManager
from api_warehouse.api_warehouse import APIWarehouse
from crawlers.player_crawler import PlayerCrawler
from crawlers.stadium_crawler import StadiumCrawler
from crawlers.team_crawler import TeamCrawler
from matches_manager.matches_manager import MatchesManager
from matches_manager.matches_manager_factory import MatchesManagerFactory
from warehouse.model import Model
from warehouse.warehouse_error import WarehouseError

load_dotenv()

class Rastreator:
    """ Clase para controlar todos los crawlers que se utilizan  """

    def __init__(self):
        self._warehouse = APIWarehouse()
        self._matches_manager_factory = MatchesManagerFactory()
        self._model_manager = APIModelManager()

    def scrap_teams(self):
        crawler = TeamCrawler(self._model_manager)
        teams_matches_manager = self._matches_manager_factory.get_team_matches_manager()

        for team in crawler.get_scraped_teams():
            try:
                self._save_model(teams_matches_manager, team)

            except WarehouseError as e:
                print(f"Error al guardar equipo {team.get_value_for('Nombre corto')}")
                print(e)

        teams_matches_manager.flush()

    def _save_model(self, matches_manager: MatchesManager, model: Model, override=False) -> int:
        if matches_manager.exists(model.get_key_for_matches_manager()):
            match_id = matches_manager.get_match_id(model.get_key_for_matches_manager())
            if override:
                self._warehouse.update_model(match_id, model)

            return match_id

        match_id = self._warehouse.save_model(model)
        matches_manager.save_match(model.get_key_for_matches_manager(), match_id)

        return match_id

    def scrap_stadiums(self) -> None:
        teams_matches_manager = self._matches_manager_factory.get_team_matches_manager()
        crawler = StadiumCrawler(self._model_manager)
        stadium_matches_manager = self._matches_manager_factory.get_stadium_matches_manager()

        for stadium in crawler.get_scraped_stadiums():
            try:
                id_team = teams_matches_manager.get_match_id(stadium.get_value_for('Equipo'))
                id_stadium = self._save_model(stadium_matches_manager, stadium)

                self._warehouse.set_current_stadium_of_team(id_stadium, id_team)

            except WarehouseError as e:
                print(f"Ha ocurrido un error al guardar el estadio {stadium}")
                print(e)

        stadium_matches_manager.flush()

    def scrap_players(self) -> None:
        teams_crawler = TeamCrawler(self._model_manager)
        player_crawler = PlayerCrawler(self._model_manager)
        player_matches_manager = self._matches_manager_factory.get_player_matches_manager()
        teams_matches_manaher = self._matches_manager_factory.get_team_matches_manager()

        for team in teams_crawler.get_scraped_teams():
            url = team.get_value_for('URL del equipo en RF')
            print(f"Rastreando jugadores de {team.get_value_for('Nombre completo')}...")
            squad = []
            for player in player_crawler.get_scraped_players_of_team(url[url.rfind("/") + 1:]):
                try:
                    squad.append({
                        'id': self._save_model(player_matches_manager, player),
                        'dorsal': player.get_value_for('Dorsal')
                    })

                except WarehouseError as e:
                    print(f"Ha ocurrido un error al guardar el jugador, {player}")
                    print(e)

            squad_id = self._warehouse.save_squad(squad)
            self._warehouse.associate_team_squad_competition(
                teams_matches_manaher.get_match_id(team.get_key_for_matches_manager()),
                squad_id,
                int(os.getenv('COMPETITION_ID'))
            )

        player_matches_manager.flush()
