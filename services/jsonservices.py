import json

from modelos.modelable import Modelable


def json_serializer(filename: str, data_list: list[Modelable]):
    with open(filename, 'w') as file:
        json.dump([item.json_serialize() for item in data_list], file)


def json_unserializer(filename: str) -> list:
    pass
