from datetime import datetime

from url import Urls
from sopa import Sopa
from modelos.jornada import Jornada
from modelos.partido import Partido
from almacenes.almacen_jornadas import AlmacenJornadas
from exceptions.invalid_key_error import InvalidKeyError


class RastreadorCalendario:
    def __init__(self, almacen: AlmacenJornadas):
        self._jornadas = {}
        self._almacen = almacen

    def rastrea_calendario(self) -> None:
        sopa = Sopa(Urls.url_calendario()).get_sopa()

        for html in sopa.select('.col-calendar-content .boxhome'):
            titulo_jornada = html.find('span', class_='titlebox').text
            jornada = Jornada()
            jornada.set_numero(int(titulo_jornada.split(' ')[1]))

            for tr in html.find_all('tr'):
                partido = Partido()
                partido.set_equipo_local(tr.find('td', class_='equipo1').text)
                partido.set_equipo_visitante(tr.find('td', class_='equipo2').text)
                partido.set_fecha(datetime.fromisoformat(tr.find('span', class_='dtstart').text))

                jornada.agrega_partido(partido)

            self._almacen.save(jornada)

            print(f"Jornada {jornada.get_numero()} rastreada")

    def visualiza_jornada(self):
        if not self._jornadas:
            self._jornadas = self._almacen.load_all()

        numero = int(input('Numero de jornada: '))
        if numero not in self._jornadas.keys():
            raise InvalidKeyError(numero)

        (self._jornadas.get(numero)).ver_jornada()
        espera = input()
