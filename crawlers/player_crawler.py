from icecream import ic

from sopa import Sopa
from url import Urls
from warehouse.model import Model
from warehouse.model_manager import ModelManager


class PlayerCrawler:

    def __init__(self, model: ModelManager):
        self._model_manager = model

    def get_scraped_players_of_team(self, team: str) -> list[Model]:
        html_pantilla = Sopa(Urls.url_plantilla_page(team)).get_sopa()

        scraped_players: list[Model] = []

        for player_el in html_pantilla.find_all('tr', attrs={'itemprop': 'employee'})[:1]:
            scraped_players.append(self.scrap_player(f"{Urls.dominio}{player_el.a['href']}"))

        return scraped_players

    def scrap_player(self, url: str) -> Model:
        sopa = Sopa(url).get_sopa()

        player = self._model_manager.get_player_model()

        for el in sopa.find_all(['dt', 'dd']):
            if el.string in player.get_available_fields_for_crawler():
                ic(el.string, el.next_sibling)
        return player
