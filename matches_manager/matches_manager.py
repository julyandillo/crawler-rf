import json
from os.path import isfile

from .matches_manager_error import MatchesManagerError


class MatchesManager:
    """
    Clase para guardar la relación entre id/clave almacenada en un almacén y id/clave de la web resultados-futbol.com
    """
    def __init__(self, filename: str):
        self._filename = filename if filename.endswith('.json') else f"{filename}.json"
        self._matches = {}

        if isfile(filename):
            with open(filename, 'r') as file:
                self._matches = json.load(file)

    def flush(self):
        with open(self._filename, 'w') as file:
            json.dump(self._matches, file, indent=2, sort_keys=True)

    def save_match(self, key: int | str, match_id: int) -> None:
        self._matches[key] = match_id

    def get_match_id(self, key: int | str) -> int:
        if key not in self._matches.keys():
            raise MatchesManagerError(f"No existe ningún match asociado para la clave '{key}'")

        return self._matches.get(key)

    def exists(self, key) -> bool:
        return key in self._matches.keys()

    def load_all(self) -> iter:
        return self._matches.keys()
