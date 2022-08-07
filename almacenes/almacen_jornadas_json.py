from almacenes.almacen_jornadas import AlmacenJornadas
from modelos.jornada import Jornada
from services.json_services import save_as_json, load_from_json
from utils.utils import generate_dict_from_list
from exceptions.invalid_key_error import InvalidKeyError
from builders.jornada_builder import JornadaBuilder


FILE_NAME = 'jornadas.json'


class AlmacenJornadasJson(AlmacenJornadas):
    def __init__(self):
        self._jornadas = {}

    def save(self, jornada: Jornada) -> None:
        self._jornadas[jornada.get(Jornada.get_json_structure().key)] = jornada
        save_as_json(FILE_NAME, list(self._jornadas.values()))

    def load(self, numero_jornada: int) -> Jornada:
        if not self._jornadas:
            self.load_all()

        if numero_jornada not in self._jornadas.keys():
            raise InvalidKeyError(numero_jornada)

        return self._jornadas.get(numero_jornada)

    def load_all(self) -> dict:
        self._jornadas = generate_dict_from_list(
            Jornada.get_json_structure().key,
            [JornadaBuilder(jornada_almacenada).get_jornada() for jornada_almacenada in load_from_json(FILE_NAME)])

        return self._jornadas
