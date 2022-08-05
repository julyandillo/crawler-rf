from modelos.estadio import Estadio
from sopa import Sopa


def rastrea_estadio(url: str) -> Estadio:
    sopa = Sopa(url).get_sopa()
    estadio = Estadio()

    for li in sopa.select('.bi-stadium li'):
        spans = li("span")
        if spans[0].text in estadio.get_lista_datos_necesarios():
            # print(f"{spans[0].text}: {spans[1].text}")
            estadio.guarda(spans[0].text, spans[1].text)

    for li in sopa.select('#text1 li'):
        spans = li("span")
        if spans[0].text == 'Ciudad':
            estadio.set_ciudad(spans[1].text)

    return estadio
