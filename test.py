import json

import requests
from bs4 import BeautifulSoup

from matches_manager.matches_manager_factory import MatchesManagerFactory


def main():
    url = "https://es.besoccer.com/ajax/rounds?id=1&round={round}&league=76448&group=1&year=2025&isCompetition=1&competition=1"
    matches_manager = MatchesManagerFactory()
    teams = matches_manager.get_team_matches_manager()

    for jornada in range(1):
        response = requests.get(url.format(round=jornada))
        if response.status_code != 200:
            print(f"Error al obtener la jornada {jornada}")
            continue

        print(f"Jornada {jornada}")
        s = BeautifulSoup(response.text, 'lxml')
        for el in s.select('.match-link script[type="application/ld+json"]'):
            content = json.loads(el.text)
            home_team = content['homeTeam']['name']
            away_team = content['awayTeam']['name']
            print(
                f"\t{home_team}[{teams.get_match_id(home_team)}] - {away_team}[{teams.get_match_id(away_team)}] | {content['startDate']}")


if __name__ == '__main__':
    main()
