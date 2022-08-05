"""
Namedtuple para poder configurar la estructura de como serán los jsons. Básicamente se define un campo saber cual
 será la key y el valor del diccionario que se creará para guardarlo como json
"""
from collections import namedtuple


JsonStructure = namedtuple('JsonStructure', 'key values')
