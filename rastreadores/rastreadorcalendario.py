from datetime import datetime

from url import Urls
from sopa import Sopa
from modelos.jornada import Jornada
from modelos.partido import Partido
from exceptions.InvalidKeyError import InvalidKeyError


class RastreadorCalendario:
    def __init__(self):
        self.jornadas = {}

    def rastrea_calendario(self) -> None:
        sopa = Sopa(Urls.url_calendario()).get_sopa()

        for html in sopa.select('.col-calendar-content .boxhome'):
            titulo_jornada = html.find('span', class_='titlebox').text
            jornada = Jornada(int(titulo_jornada.split(' ')[1]))

            for tr in html.find_all('tr'):
                partido = Partido()
                partido.equipo_local = tr.find('td', class_='equipo1').text
                partido.equipo_visitante = tr.find('td', class_='equipo2').text
                partido.fecha = datetime.fromisoformat(tr.find('span', class_='dtstart').text)

                jornada.agrega_partido(partido)

            self.jornadas[jornada.numero] = jornada
            print(f"Jornada {jornada.numero} rastreada")

    def visualiza_jornada(self):
        numero = int(input('Numero de jornada: '))
        if numero not in self.jornadas.keys():
            raise InvalidKeyError(numero)

        (self.jornadas.get(numero)).ver_jornada()
        espera = input()
