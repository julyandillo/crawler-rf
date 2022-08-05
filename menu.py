from consolemenu import ConsoleMenu
from consolemenu.items import MenuItem, SubmenuItem, FunctionItem

from rastreadores.rastreador_equipo import RastreadorEquipos
from rastreadores.rastreador_calendario import RastreadorCalendario
from almacenes.almacenes_factory import AlmacenesFactory


class Menu:
    _menu: ConsoleMenu

    def __init__(self):
        self._menu = ConsoleMenu("Crawler resultados-futbol.com")

        rastreador_equipos = RastreadorEquipos(AlmacenesFactory.get_almacen_equipos())
        rastreador_calendario = RastreadorCalendario(AlmacenesFactory.get_almacen_jornadas())

        item_rastrea_equipos = FunctionItem("Rastrea equipos", rastreador_equipos.rastrea_equipos)
        item_rastrea_calendario = FunctionItem("Rastrea calendario", rastreador_calendario.rastrea_calendario)

        menu_rastrea = ConsoleMenu("Rastrea")
        menu_rastrea.append_item(item_rastrea_equipos)
        menu_rastrea.append_item(item_rastrea_calendario)

        submenu_rastrea = SubmenuItem("Rastrea", menu_rastrea)

        item_muestra_equipos = FunctionItem("Muestra equipos rastreados",
                                            rastreador_equipos.visualiza_equipos_rastreados)
        item_muestra_jornada = FunctionItem("Ver jornada", rastreador_calendario.visualiza_jornada)

        menu_visualizacion = ConsoleMenu("Visualización de datos rastreados")
        menu_visualizacion.append_item(item_muestra_equipos)
        menu_visualizacion.append_item(item_muestra_jornada)

        submenu_visualizacion = SubmenuItem("Visualización de datos rastreados", menu_visualizacion)

        menu_api = MenuItem("API")

        self._menu.append_item(submenu_rastrea)
        self._menu.append_item(submenu_visualizacion)
        self._menu.append_item(menu_api)

    def muestra_menu(self):
        self._menu.show()
