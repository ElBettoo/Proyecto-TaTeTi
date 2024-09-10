from abc import ABC, abstractmethod
from tablero.tablero_structure.tablero_structure import TableroStructure
from tablero.tablero_structure.casillero import Casillero

class TatetiVictoryPattern:
    @abstractmethod
    def get_possible_cords_by_last_move(self, tablero_structure: TableroStructure, last_move: tuple[int, int], win_length) -> list[Casillero]:
        pass