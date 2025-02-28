from typing import Self, Callable

from exceptions.invalid_field_error import InvalidFieldError
from .field import Field


class Model:
    """
    Clase que almacena en un diccionario todos los campos rastreados por cada rastreador.
    El diccionario tendrá como clave el nombre del campo del rastreador y como valor una instancia de la clase Field
     """
    VALUE_NOT_PARSED = 'Value not parsed'

    TEAM_TYPE = 'team'
    STADIUM_TYPE = 'stadium'
    PLAYER_TYPE = 'player'
    MATCH_TYPE = 'match'

    def __init__(self, *, fields: list[Field], key_matches_manager='', key_string: str | Callable | None = None,
                 model_type: str | None = None):
        self._available_fields = {field.crawler_name: field for field in fields}
        self._available_field_list = self._available_fields.keys()
        self._key_for_matches_manager = key_matches_manager
        self._key_string = key_string
        self._model_type = model_type

    def add_field(self, field: Field) -> Self:
        self._available_fields[field.crawler_name] = field

        if field.crawler_name not in self._available_field_list:
            self._available_field_list = self._available_fields.keys()

        return self

    def set_fields(self, fields: list[Field]):
        for field in fields:
            self.add_field(field)

    def get_available_fields_for_crawler(self) -> iter:
        return self._available_field_list

    def set_value_for(self, name: str, value: str) -> Self:
        if name not in self._available_field_list:
            raise InvalidFieldError(name)

        self._available_fields[name].set_value(value)
        return self

    def get_value_for(self, name: str) -> str | int | float:
        if name not in self._available_field_list:
            raise InvalidFieldError(name)

        return self._available_fields[name].value or self.VALUE_NOT_PARSED

    def get_key_for_matches_manager(self) -> str:
        if self._key_for_matches_manager not in self._available_field_list:
            raise InvalidFieldError(f"The field '{self._key_for_matches_manager}' cannot be used as key matches", True)

        return self._available_fields[self._key_for_matches_manager].value

    def prepare(self) -> dict:
        return {field.target_name: field.value for field in self._available_fields.values() if
                field.target_name is not None and field.value is not None}

    def get_type(self) -> None | str:
        return self._model_type

    def __repr__(self):
        return f"{self._available_fields}"

    def __str__(self):
        if callable(self._key_string):
            return self._key_string(self)

        if isinstance(self._key_string, str):
            return f"{self._key_string}: {self._available_fields[self._key_string].value}"

        return "\n".join([f"{name}: {field.value}" for name, field in self._available_fields.items()])
