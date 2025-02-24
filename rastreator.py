from api_warehouse.api_model_manager import APIModelManager
from api_warehouse.api_warehouse import APIWarehouse
from crawlers.player_crawler import PlayerCrawler
from crawlers.stadium_crawler import StadiumCrawler
from crawlers.team_crawler import TeamCrawler
from matches_manager.matches_manager import MatchesManager
from matches_manager.matches_manager_factory import MatchesManagerFactory
from warehouse.model import Model
from warehouse.warehouse_error import WarehouseError


class Rastreator:
    """ Clase para controlar todos los crawlers que se utilizan  """

    def __init__(self):
        self._warehouse = APIWarehouse()
        self._matches_manager_factory = MatchesManagerFactory()
        self._model_manager = APIModelManager()

    def scrap_teams(self):
        crawler = TeamCrawler(self._model_manager)
        teams = crawler.get_scraped_teams()

        self._save_teams(teams)

    def _save_teams(self, teams: list[Model]):
        team_matches_manager = self._matches_manager_factory.get_team_matches_manager()

        for team in teams:
            try:
                id_team = team_matches_manager.load_id_warehouse(team.get_key_for_matches_manager())
                if id_team == MatchesManager.NOT_EXISTS:
                    id_team = self._warehouse.save_team(team)
                else:
                    self._warehouse.update_team(id_team, team)

                team_matches_manager.save_match(team.get_key_for_matches_manager(), id_team)

            except WarehouseError as e:
                print(f"Error al guardar equipo {team.get_value_for('Nombre corto')}")
                print(e)

        team_matches_manager.flush()

    def scrap_stadiums(self) -> None:
        teams_matches_manager = self._matches_manager_factory.get_team_matches_manager()
        crawler = StadiumCrawler(self._model_manager)

        for stadium in crawler.get_scraped_stadiums():
            try:
                id_team = teams_matches_manager.load_id_warehouse(stadium.get_value_for('Equipo'))
                self._save_stadium(stadium, id_team)

            except WarehouseError as e:
                print(e)

    def _save_stadium(self, stadium: Model, id_team: int):
        matches_manager = self._matches_manager_factory.get_stadium_matches_manager()

        id_stadium = matches_manager.load_id_warehouse(stadium.get_key_for_matches_manager())
        if id_stadium == MatchesManager.NOT_EXISTS:
            id_stadium = self._warehouse.save_stadium(stadium)
            matches_manager.save_match(stadium.get_key_for_matches_manager(), id_stadium)
            matches_manager.flush()
        else:
            self._warehouse.update_stadium(id_stadium, stadium)

        self._warehouse.set_stadium_for_team(id_stadium, id_team)

    def scrap_players(self) -> None:
        # teams_crawler = TeamCrawler(self._model_manager)
        player_crawler = PlayerCrawler(self._model_manager)
        # matches_manager = self._matches_manager_factory.get_player_matches_manager()

        # for team in teams_crawler.get_scraped_teams()[:1]:
        #    url = team.get_value_for('URL del equipo en RF')
        #    players = player_crawler.get_scraped_players_of_team(url[url.rfind("/")+1:])

        players = player_crawler.get_scraped_players_of_team('Athletic-Bilbao')
        for player in players:
            print(player)
