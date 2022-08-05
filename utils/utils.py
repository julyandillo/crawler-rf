from datetime import datetime

from modelos.modelable import Modelable


def generate_dict_from_list(key: str, teams: list[Modelable]):
    """
    genera un diccionario recorriendo la lista, la key sera el valor del campo del objeto cuya key se pasa
    como parametro, el valor será el propio objeto
    """
    return {team.get(key): team for team in teams}


def date_format(date: datetime) -> str:
    return date.strftime('%d-%m-%Y')
