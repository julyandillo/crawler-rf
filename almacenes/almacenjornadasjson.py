from almacenes.almacenjornadas import AlmacenJornadas
from modelos.jornada import Jornada
from services.jsonservices import save_as_json, load_from_json
from utils.utils import generate_dict_from_list
from exceptions import InvalidKeyError


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
        self._jornadas = generate_dict_from_list(Jornada.get_json_structure().key,
                                                 [self._crea_jornada(jornada) for jornada in load_from_json(FILE_NAME)])
        return self._jornadas

    def _crea_jornada(self, jornada_almacenada: dict) -> Jornada:
        jornada = Jornada()
        for key, value in jornada_almacenada.items():
            jornada.set(key, value)
        # jornada.set('fecha_inicio', jornada_almacenada['fecha_inicio'])
        # jornada.set('fecha_fin', jornada_almacenada['fecha_fin'])
        return jornada
