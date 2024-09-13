
from tablero.tablero_structure.casillero import Casillero
from tablero.tablero_structure.tablero_structure import TableroStructure
from victory_checker.tateti_patterns.tateti_victory_pattern import TatetiVictoryPattern


class TatetiCornersChecker(TatetiVictoryPattern):
    
    def get_possible_cords_by_last_move(self, cantidad_casilleros: tuple[int, int], last_move: tuple[int, int], win_length: tuple[int, int]) -> list[Casillero]:
        cantidad_columnas, cantidad_filas = cantidad_casilleros
        corners = [(0,0), (0,cantidad_filas-1), (cantidad_columnas-1, 0), (cantidad_columnas-1, cantidad_filas-1)] # Todas las cordenadas de las esquinas

        return [corners], len(corners)

