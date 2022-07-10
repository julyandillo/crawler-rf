from modelos.equipo import Equipo
from sopa import Sopa


def rastrea_equipo(url: str) -> Equipo:
    sopa = Sopa(url).get_sopa()

    equipo_rastreado = Equipo()

    for li in sopa.select('#text1 li'):
        spans = li("span")
        if spans[0].text in equipo_rastreado.get_lista_datos_necesarios():
            # print(f"{spans[0].text}: {spans[1].text}")
            equipo_rastreado.guarda(spans[0].text, spans[1].text)

    return equipo_rastreado
