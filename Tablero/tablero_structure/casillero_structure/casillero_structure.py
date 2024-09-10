from abc import ABC, abstractmethod
from tablero.tablero_structure.casillero import Casillero

class CasilleroStructure(ABC):
    def __init__(self, pattern: list[Casillero]):
        self.__casillero_structure = []
        self.__pattern = pattern # Patron de casilleros que se quiera seguir

    @abstractmethod
    def create_casilleros(self, cantidad_casilleros: tuple[int, int]):
        pass