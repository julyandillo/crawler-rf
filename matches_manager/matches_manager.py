import json
from os.path import isfile


class MatchesManager:
    """
    Clase para guardar la relación entre id/clave almacenada en un almacén y id/clave de la web resultados-futbol.com
    """
    NOT_EXISTS = -1

    def __init__(self, filename: str):
        self._filename = filename if filename.endswith('.json') else f"{filename}.json"
        self._matches = {}

        if isfile(filename):
            with open(filename, 'r') as file:
                self._matches = json.load(file)

    def flush(self):
        with open(self._filename, 'w') as file:
            json.dump(self._matches, file, indent=2, sort_keys=True)

    def save_match(self, key: int | str, id_warehouse: int) -> None:
        self._matches[key] = id_warehouse

    def load_id_warehouse(self, key: int | str) -> int:
        return self._matches.get(key, self.NOT_EXISTS)

    def load_all(self) -> iter:
        return self._matches.keys()
