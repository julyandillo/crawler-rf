from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem, SubmenuItem

from rastreator import Rastreator


class Menu:
    """ Clase para generar el menú y controlar los crawlers """
    def __init__(self):
        self._rastreator = Rastreator()
        self._menu = ConsoleMenu("Crawler resultados-futbol.com")

        # rastreador_calendario = RastreadorCalendario(AlmacenesFactory.get_almacen_jornadas())

        # item_rastrea_calendario = FunctionItem("Rastrea calendario", rastreador_calendario.rastrea_calendario)

        submenu_rastrea = ConsoleMenu("Rastreador")
        item_rastrea_equipos = FunctionItem("Rastrea equipos", self._rastreator.scrap_teams)

        submenu_rastrea.append_item(item_rastrea_equipos)
        # item_muestra_jornada = FunctionItem("Ver jornada", rastreador_calendario.visualiza_jornada)

        submenuitem_rastrea = SubmenuItem("Rastreador", submenu_rastrea, self._menu)

        self._menu.append_item(submenuitem_rastrea)

    def muestra_menu(self):
        self._menu.show()
