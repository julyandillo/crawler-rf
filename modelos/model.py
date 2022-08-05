from exceptions.invalid_key_error import InvalidKeyError


class Model:
    def __init__(self, available_fields_list: list):
        self.available_fields_list = available_fields_list
        self._model = {}

    def get_available_fields_list(self) -> list:
        return self.available_fields_list

    def set(self, key: str, valor: str | int | float):
        if key not in self.available_fields_list:
            raise InvalidKeyError(key)

        self._model[key] = valor

    def get(self, key: str) -> str | int | float:
        if key not in self.available_fields_list:
            raise InvalidKeyError(key)

        # es posible que aún existiendo en los campos disponibles no se haya podido rastrear y no este en el dict
        return self._model.get(key, 'Información no rastreada')

    def get_modelo(self) -> dict:
        return self._model
