from sopa import Sopa
from url import Urls
from warehouse.model import Model
from warehouse.model_manager import ModelManager


class StadiumCrawler:
    def __init__(self, model_manager: ModelManager):
        self._model_manager = model_manager

    def scrap_stadium(self, url: str) -> Model:
        sopa = Sopa(url).get_sopa()

        stadium = self._model_manager.get_stadium_model()
        stadium.set_value_for('Nombre', sopa.find('div', class_='head-title').text.strip())

        team_name = sopa.find('div', class_='team-text').b
        stadium.set_value_for('Equipo', team_name.text.strip() if team_name is not None else 'Barcelona')

        for row in sopa.select('#mod_stadium_stats .panel-body .table-body .table-row'):
            divs = row('div')
            key = divs[0].text
            if key in stadium.get_available_fields_for_crawler():
                content = divs[1].text.strip()
                stadium.set_value_for(key, content if key != 'Capacidad' else content.split(' ')[0].replace('.', ''))

        return stadium

    def get_scraped_stadiums(self) -> list[Model]:
        html_stadiums = Sopa(Urls.url_stadiums_page()).get_sopa()
        scraped_stadiums = []

        for stadium_box in html_stadiums.select('div.stadiums.box>.panel'):
            stadium_page = stadium_box.find('a')['href']
            stadium = self.scrap_stadium(stadium_page)
            print(f"Nuevo estadio rastreado: {str(stadium)}")

            scraped_stadiums.append(stadium)

        return scraped_stadiums
