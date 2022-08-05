from sopa import Sopa

from modelos.equipo import Equipo
from url import Urls
from almacenes.almacen_equipos import AlmacenEquipos


def rastrea_equipo(url: str) -> Equipo:
    sopa = Sopa(url).get_sopa()

    equipo_rastreado = Equipo()

    for li in sopa.select('#text1 li'):
        spans = li("span")
        if spans[0].text in equipo_rastreado.get_lista_campos_disponibles():
            # print(f"{spans[0].text}: {spans[1].text}")
            equipo_rastreado.set(spans[0].text, spans[1].text)

    return equipo_rastreado


class RastreadorEquipos:
    _equipos_rastreados: list

    def __init__(self, almacen: AlmacenEquipos):
        self._equipos_rastreados = []
        self._almacen = almacen

    def rastrea_equipos(self):
        equipos = Sopa(Urls.url_pagina_equipos()).get_sopa()

        for url_equipo in equipos('td', class_="equipo"):
            equipo = rastrea_equipo(Urls.dominio + url_equipo.a['href'])
            if equipo:
                print(f"{equipo} rastreado")
                self._equipos_rastreados.append(equipo)

        self._almacen.save_all_teams(self._equipos_rastreados)
        print(*self._equipos_rastreados, sep='\n')

    def visualiza_equipos_rastreados(self):
        equipo = input('Nombre corto del equipo: ')
        print(self._almacen.load_team(equipo))

        espera = input()
