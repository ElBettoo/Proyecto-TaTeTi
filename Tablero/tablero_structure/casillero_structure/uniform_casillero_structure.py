from tablero.tablero_structure.casillero_structure.casillero_structure import CasilleroStructure
from tablero.casillero import Casillero

class UniformCasilleroStructure(CasilleroStructure):
    def __init__(self, pattern: list[Casillero]):
        super().__init__(pattern)
        self.__casillero_structure = []
        self.__pattern = pattern

    def create_casilleros(self, cantidad_casilleros: tuple[int, int]):
        cantidad_filas, cantidad_columnas = cantidad_casilleros
        self.__casillero_structure = [[self.__pattern[0](column, row) for column in range(cantidad_columnas)] for row in range(cantidad_filas)]

        return self.__casillero_structure