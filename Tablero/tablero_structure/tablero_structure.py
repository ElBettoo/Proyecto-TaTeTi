from .casillero import Casillero
from tablero.tablero_structure.casillero_structure.casillero_structure import CasilleroStructure
from tablero.tablero_structure.tablero_creator.tablero_creator import TableroCreator
from tablero.tablero_structure.piece_structure.piece_structure import PieceStructure
from tablero.tablero_iterator.tablero_structure_iterator import TableroStructureIterator
from tablero.objects.tablero_object import TableroObject
from collections.abc import Iterable

class TableroStructure(Iterable): 
    """ Clase encargada de almacenar toda la estructura del tablero, incluyendo los casilleros y las piezas """

    def __init__(self, casillero_structure: CasilleroStructure, piece_structure: PieceStructure, cantidad_casilleros: tuple[int, int]): # cantidad_casilleros = (rows, columns)  EJ: 4x4
        if not piece_structure.check_compatibility(cantidad_casilleros):
            raise Exception("Not Compatible")

        self.__cantidad_casilleros = cantidad_casilleros
        self.__casillero_structure = casillero_structure
        self.__piece_structure = piece_structure
        self.__tablero_creator = TableroCreator()
        self.__casilleros_data = self.crear_tablero()

    def create_casilleros(self) -> list[list[Casillero]]:  # Devuelve la matriz solamente con casilleros 
        return self.__casillero_structure.create_casilleros(self.__cantidad_casilleros)

    def get_starting_pieces(self) -> list[list[TableroObject]]: # Devuelve la matriz solamente con piezas
        return self.__piece_structure.get_starting_pieces(self.__cantidad_casilleros)

    def crear_tablero(self) -> list[list[Casillero]]:
        casilleros_tablero = self.create_casilleros()
        piezas_tablero = self.get_starting_pieces()

        return self.__tablero_creator.crear_tablero(casilleros_tablero, piezas_tablero, self.__cantidad_casilleros)

    def __iter__(self) -> TableroStructureIterator:
        return TableroStructureIterator(self.casilleros_data)

    @property
    def casilleros_data(self):
        return self.__casilleros_data

    @property
    def cantidad_casilleros(self):
        return self.__cantidad_casilleros

    