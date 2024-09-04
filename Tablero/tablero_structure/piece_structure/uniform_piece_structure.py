from tablero.tablero_structure.piece_structure.dinamic_piece_structure import DinamicPieceStructure
from tablero.objects.tablero_object import TableroObject

class UniformPieceStructure(DinamicPieceStructure):
    def __init__(self, ObjectPattern: list[TableroObject]):
        super().__init__(ObjectPattern)
        self.__pattern = ObjectPattern # Patron de objetos que se quiera seguir
        if len(self.__pattern) != 1:
            raise Exception("'UniformPieceStructure' only works with 1 object")

    def get_starting_pieces(self, cantidad_casilleros: tuple[int, int]):
        cantidad_filas, cantidad_columnas = cantidad_casilleros
        self.__starting_position = [[self.__pattern[0]() for column in range(cantidad_columnas)] for row in range(cantidad_filas)]

        return self.__starting_position