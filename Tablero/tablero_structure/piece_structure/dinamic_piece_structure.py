from abc import ABC, abstractmethod
from tablero.tablero_structure.piece_structure.piece_structure import PieceStructure
from tablero.objects.tablero_object import TableroObject

class DinamicPieceStructure(PieceStructure): # Significa que la estructura se adapta a la cantidad de casilleros del tablero
    def __init__(self, ObjectPattern: list[TableroObject]):
        self.__pattern = ObjectPattern # Patron de objetos que se quiera seguir
        self.__starting_position = []
        self.__always_compatible = True

    def check_compatibility(self, cantidad_casilleros: tuple[int, int]):
        return self.__always_compatible

    @abstractmethod
    def get_starting_pieces(self, cantidad_casilleros: tuple[int, int]):
        pass 