from modelos.equipo import Equipo
from sopa import Sopa
from url import Urls


def rastrea_equipo(url: str) -> Equipo:
    sopa = Sopa(url).get_sopa()

    equipo_rastreado = Equipo()

    for li in sopa.select('#text1 li'):
        spans = li("span")
        if spans[0].text in equipo_rastreado.get_lista_datos_necesarios():
            # print(f"{spans[0].text}: {spans[1].text}")
            equipo_rastreado.guarda(spans[0].text, spans[1].text)

    return equipo_rastreado


class RastreadorEquipos:
    _equipos_rastreados: list

    def __init__(self):
        self._equipos_rastreados = []

    def rastrea_equipos(self):
        equipos = Sopa(Urls.url_pagina_equipos()).get_sopa()

        for url_equipo in equipos('td', class_="equipo"):
            equipo = rastrea_equipo(Urls.dominio + url_equipo.a['href'])
            if equipo:
                print(f"{equipo} rastreado")
                self._equipos_rastreados.append(equipo)

    def visualiza_equipos_rastreados(self):
        for equipo in self._equipos_rastreados:
            print(equipo)
            input()
