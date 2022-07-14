from url import Urls
from sopa import Sopa
from rastreadores.rastreadorequipo import rastrea_equipo
from rastreadores.rastreadorestadio import rastrea_estadio
from menu import Menu


def main():
    menu = Menu()
    menu.muestra_menu()


def main_v():
    equipos = Sopa(Urls.url_pagina_equipos()).get_sopa()

    for url_equipo in equipos('td', class_="equipo"):
        equipo = rastrea_equipo(Urls.dominio + url_equipo.a['href'])
        print(f"{equipo} rastreado")

        estadio = rastrea_estadio(Urls.dominio + url_equipo.a['href'])
        estadio.set_ciudad(equipo.get_ciudad())
        print(f"Estadio: {estadio}")


if __name__ == '__main__':
    main()
