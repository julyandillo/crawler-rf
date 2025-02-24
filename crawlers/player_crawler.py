import gettext

import pycountry

from sopa import Sopa
from url import Urls
from warehouse.model import Model
from warehouse.model_manager import ModelManager

# para generar las traducciones de los países
spanish = gettext.translation('iso3166-1', pycountry.LOCALES_DIR, languages=['es'])
spanish.install()

class PlayerCrawler:

    def __init__(self, model: ModelManager):
        self._model_manager = model

    def get_scraped_players_of_team(self, team: str) -> list[Model]:
        html_pantilla = Sopa(Urls.url_plantilla_page(team)).get_sopa()

        scraped_players: list[Model] = []

        for player_el in html_pantilla.find_all('tr', attrs={'itemprop': 'employee'}):
            scrap_player = self.scrap_player(f"{Urls.dominio}{player_el.a['href']}")
            # el dorsal en la página del jugador a veces no es el mismo que en la lista de la plantilla
            scrap_player.set_value_for('Dorsal', player_el.find('td', class_='num').text)

            # en la página del jugador cuando no tiene ficha del primer equipo aparece el nombre del filial
            scrap_player.set_value_for('Equipo', html_pantilla.h1.text)

            scraped_players.append(scrap_player)


        return scraped_players

    def scrap_player(self, url: str) -> Model:
        sopa = Sopa(url).get_sopa()

        player = self._model_manager.get_player_model()
        el = sopa.select_one('.info.position')
        # a veces puede aparecer más de un '.' con lo que son más de 2 valores para desempaquetar
        dorsal, posicion, *d = map(str.strip, el.text.split('.'))

        for el in sopa.find('dl').children:
            field_name = el.text
            if field_name in player.get_available_fields_for_crawler():
                next_sibling = el.find_next_sibling('dd')
                if field_name == 'Nombre' and player.get_value_for(field_name) != player.VALUE_NOT_PARSED:
                    # el nombre que nos interesa es el primero (lo que sería el apodo)
                    pass
                elif field_name == 'Lugar de nacimiento':
                    isocode = (next_sibling.find('img').attrs['alt'].split('-')[1]).strip().upper()
                    country = pycountry.countries.get(alpha_2=isocode)
                    player.set_value_for(field_name, _(country.name))
                else:
                    player.set_value_for(field_name, next_sibling.text.strip())
        return player
