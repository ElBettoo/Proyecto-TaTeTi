from abc import ABC, abstractmethod
from piece_structure import PieceStructure
from tablero.objects.tablero_object import TableroObject

class StaticPieceStructure(ABC, PieceStructure): # Significa que la estructura no se adapta a la cantidad de casilleros del tablero, como en el ajedrez que es siempre 8x8 
    def __init__(self):
        self.__starting_position = list[list[TableroObject]] # Matriz con cada pieza asignada a su casillero correspondiente 
        self.__always_compatible = False

    def check_compatibility(self, cantidad_casilleros: tuple[int, int]):
        cantidad_filas, cantidad_columnas = cantidad_casilleros
        return (cantidad_filas == len(self.__starting_position)) and (cantidad_columnas == len(self.__starting_position[0]))

    def get_starting_pieces(self):
        return self.__starting_position