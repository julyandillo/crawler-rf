from sopa import Sopa
from url import Urls
from warehouse.model import Model
from warehouse.model_manager import ModelManager


class TeamCrawler:

    def __init__(self, model_manager: ModelManager):
        self._model_manager = model_manager

    def scrap_team(self, url: str) -> Model:
        sopa = Sopa(url).get_sopa()

        team = self._model_manager.get_team_model()

        for li in sopa.select('#text1 li'):
            spans = li("span")
            if spans[0].text in team.get_available_fields_for_crawler():
                # print(f"{spans[0].text}: {spans[1].text}")
                team.set_value_for(spans[0].text, spans[1].text)

        return team

    def get_scraped_teams(self) -> list[Model]:
        html_equipos = Sopa(Urls.url_pagina_equipos()).get_sopa()
        scraped_teams = []

        for url_equipo in html_equipos('td', class_="equipo"):
            team = self.scrap_team(Urls.dominio + url_equipo.a['href'])
            if team:
                print(f"Nuevo equipo rastreado: {str(team)}")
                scraped_teams.append(team)

        return scraped_teams
