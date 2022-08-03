import json

from modelos.modelable import Modelable


def json_serialize(filename: str, data_list: list[Modelable]):
    with open(filename, 'w') as file:
        json.dump([item.json_serialize() for item in data_list], file, indent=2, ensure_ascii=False)


def json_deserialize(filename: str) -> list:
    with open(filename, 'r') as file:
        return json.load(file)
