class Urls:
    dominio: str = "https://resultados-futbol.com"

    @classmethod
    def url_pagina_equipos(cls) -> str:
        return f"{cls.dominio}/primera2025/grupo1/equipos"

    @classmethod
    def url_calendario(cls) -> str:
        return f"{cls.dominio}/primera2023/grupo1/calendario"

    @classmethod
    def url_stadiums_page(cls) -> str:
        return 'https://es.besoccer.com/competicion/estadios/primera'

    @classmethod
    def url_plantilla_page(cls, team: str) -> str:
        return f"https://{cls.dominio}/plantilla/{team}"
