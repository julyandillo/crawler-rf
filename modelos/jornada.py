from modelos.partido import Partido


class Jornada:
    def __init__(self, numero: int):
        self.numero = numero
        self._partidos = []

    def __str__(self):
        return f'Jornada {self.numero}'

    def agrega_partido(self, partido: Partido):
        self._partidos.append(partido)

    def ver_jornada(self):
        print(''.ljust(50, '-'))
        print(f'Jornada {self.numero}:')
        print(''.ljust(50, '-'))
        print(*self._partidos, sep='\n')
