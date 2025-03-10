import re
from dataclasses import dataclass
from typing import Any, Callable, Literal


@dataclass(slots=True)
class Field:
    crawler_name: str
    target_name: str | None = None
    value: Any = None
    datatype: Literal['int', 'float', 'str'] = 'str'
    transform: Callable | None = None

    def set_value(self, value: str):
        match self.datatype:
            case 'int':
                self.value = int(re.sub('[^0-9]', '', value))
            case 'float':
                self.value = float(re.sub('[^0-9.]', '', value))
            case _:
                self.value = value

        if callable(self.transform):
            self.value = self.transform(self.value)
