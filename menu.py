from consolemenu import ConsoleMenu
from consolemenu.items import MenuItem, SubmenuItem, FunctionItem

from rastreadores.rastreadorequipo import RastreadorEquipos


class Menu:
    _menu: ConsoleMenu

    def __init__(self):
        self._menu = ConsoleMenu("Crawler resultados-futbol.com")

        rastreador_equipos = RastreadorEquipos()

        item_rastrea_equipos = FunctionItem("Rastrea equipos", rastreador_equipos.rastrea_equipos)
        menu_rastrea = ConsoleMenu("Rastrea")
        menu_rastrea.append_item(item_rastrea_equipos)

        submenu_rastrea = SubmenuItem("Rastrea", menu_rastrea)

        item_muestra_equipos = FunctionItem("Muestra equipos rastreados", rastreador_equipos.visualiza_equipos_rastreados)
        menu_visualizacion = ConsoleMenu("Visualización de datos rastreados")
        menu_visualizacion.append_item(item_muestra_equipos)

        submenu_visualizacion = SubmenuItem("Visualización de datos rastreados", menu_visualizacion)

        menu_api = MenuItem("API")

        self._menu.append_item(submenu_rastrea)
        self._menu.append_item(submenu_visualizacion)
        self._menu.append_item(menu_api)

    def muestra_menu(self):
        self._menu.show()