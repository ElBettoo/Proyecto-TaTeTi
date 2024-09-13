from tablero.objects.bomba_object import BombaObject
from tablero.tablero_structure.casillero import Casillero
from dataclasses import dataclass

@dataclass
class CasilleroBomba(Casillero, BombaObject):
    def __init__(self,pos_x, pos_y, piece):
        super().__init__(pos_x,pos_y,piece)
        self.__active = True