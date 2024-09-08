from tablero.objects.tablero_object import TableroObject
from dataclasses import dataclass

@dataclass
class Casillero(): #
    __pos_x: int
    __pos_y: int
    __piece: TableroObject = None

    def get_cords(self):
        return (self.__pos_x, self.__pos_y)

    @property
    def piece(self):
        return self.__piece

    def change_piece(self, new_piece: TableroObject):
        self.__piece = new_piece