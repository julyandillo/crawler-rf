"""
Namedtuple para poder configurar la estructura de como serán los jsons. Básicamente se define un campo para saber cual
 será la key y una lista con los campos del modelo que se utlizaran para crear los jsons
"""
from typing import NamedTuple


class JsonStructure(NamedTuple):
    key: str
    values: list
