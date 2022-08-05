from menu import Menu
from rastreadores.rastreador_calendario import RastreadorCalendario


def main():
    menu = Menu()
    menu.muestra_menu()


def main_v():
    calendario = RastreadorCalendario()
    calendario.rastrea_calendario()


if __name__ == '__main__':
    main()
