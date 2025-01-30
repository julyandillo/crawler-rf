from menu import Menu
from rastreator import Rastreator


def main():
    menu = Menu()
    menu.muestra_menu()


if __name__ == '__main__':
    rastreator = Rastreator()
    rastreator.scrap_players()
