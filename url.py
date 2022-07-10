class Urls:
    dominio: str = "https://resultados-futbol.com"

    @staticmethod
    def url_pagina_equipos() -> str:
        return f"{Urls.dominio}/primera2023/grupo1/equipos"

