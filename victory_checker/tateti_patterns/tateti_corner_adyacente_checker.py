
from tablero.tablero_structure.casillero import Casillero
from tablero.tablero_structure.tablero_structure import TableroStructure
from victory_checker.tateti_patterns.tateti_victory_pattern import TatetiVictoryPattern


class TatetiCornerAdyacenteChecker(TatetiVictoryPattern):
    
    def get_possible_cords_by_last_move(self, cantidad_casilleros: tuple[int, int], last_move: tuple[int, int], win_length: tuple[int, int]) -> list[Casillero]:
        cantidad_columnas, cantidad_filas = cantidad_casilleros
        corners = [(0,0), (0,cantidad_filas-1), (cantidad_columnas-1, 0), (cantidad_columnas-1, cantidad_filas-1)] # Todas las cordenadas de las esquinas

        possible_cords = []
        for cords in corners:
            cords_adyacentes = set() # set para que no se repitan las cordenadas
            cords_adyacentes.add(cords)

            for direction in [(1,0), (0,1), (-1,0), (0,-1)]: # sumo o resto 1 para encontrar los adyacentes
                x_cord = min(cantidad_columnas-1, max(0, cords[0] + direction[0]))
                y_cord = min(cantidad_filas-1, max(0, cords[1] + direction[1])) # el min y max es para que no se salga del tablero
                cords_adyacentes.add((x_cord,y_cord))
            possible_cords.append(list(cords_adyacentes))



        return possible_cords, len(cords_adyacentes)

