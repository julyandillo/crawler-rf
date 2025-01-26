from .matches_manager import MatchesManager
from .matches_manager_error import MatchesManagerError


class MatchesManagerFactory:
    TEAM_MATCHES_MANAGER = 1
    STADIUM_MATCHES_MANAGER = 2
    PLAYER_MATCHES_MANAGER = 3

    def __init__(self):
        self._matches_managers = {
            self.TEAM_MATCHES_MANAGER: 'teams.json',
            self.STADIUM_MATCHES_MANAGER: 'stadiums.json',
            self.PLAYER_MATCHES_MANAGER: 'players.json',
        }

        self._pool = {}

    def get_team_matches_manager(self) -> MatchesManager:
        return self._get_matches_manager(self.TEAM_MATCHES_MANAGER)

    def _get_matches_manager(self, name: int) -> MatchesManager:
        if name not in self._matches_managers.keys():
            raise MatchesManagerError('Not found matches manager')

        if name not in self._pool.keys():
            self._pool[name] = MatchesManager(self._matches_managers[name])

        return self._pool[name]

    def get_stadium_matches_manager(self) -> MatchesManager:
        return self._get_matches_manager(self.STADIUM_MATCHES_MANAGER)

    def get_player_matches_manager(self) -> MatchesManager:
        return self._get_matches_manager(self.PLAYER_MATCHES_MANAGER)
