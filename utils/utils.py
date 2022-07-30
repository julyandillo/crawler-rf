from modelos.modelable import Modelable


def generate_dict_teams_from_list(key: str, teams: list[Modelable]):
    return {team.get(key): team for team in teams}
