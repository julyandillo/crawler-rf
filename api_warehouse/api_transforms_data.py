import pendulum

from api_warehouse.api_error import APIError


def transform_position(position: str) -> str:
    match position.upper():
        case 'PORTERO':
            return 'POR'
        case 'DEFENSA':
            return 'DEF'
        case 'CENTROCAMPISTA':
            return 'MED'
        case 'DELANTERO':
            return 'DEL'
        case _:
            raise APIError(f"{position} no es un valor reconocido para la posición")


def transform_date(date: str) -> str:
    return pendulum.from_format(date, 'DD-MM-YYYY').strftime('%Y-%m-%d')
