from victory_checker.tateti_patterns.tateti_victory_pattern import TatetiVictoryPattern
from tablero.casillero import Casillero

class TatetiDiagonalLeftToRightChecker(TatetiVictoryPattern):

    def get_possible_cords_by_last_move(self, cantidad_casilleros: tuple[int, int], last_move: tuple[int, int], win_length) -> list[Casillero]:
        move_pos_x, move_pos_y = last_move 
        cantidad_filas, cantidad_columnas = cantidad_casilleros

        distancia_minima = min(move_pos_x, move_pos_y, win_length-1) # Valor minimo entre los casilleros para salirse del tablero en 'x' e 'y' y ademas la distancia para ganar necesaria
        start_pos_x = move_pos_x - distancia_minima
        start_pos_y = move_pos_y - distancia_minima

        full_diagonal = []
        casilleros_despues_de_last_move = 0
        #        Mientras no se salga del tablero   y   Mientras la posicion no este a 'win_length' de Last_Move
        while (start_pos_x <= cantidad_columnas-1 and start_pos_y <= cantidad_filas-1) and (casilleros_despues_de_last_move < win_length): # 2 = max_x - 1       (-1) porque el indice arranca de 0
            full_diagonal.append((start_pos_x, start_pos_y)) # Esto devuelve todas las posiciones de la diagonal entera
            start_pos_x += 1
            start_pos_y += 1

            if last_move in full_diagonal:
                casilleros_despues_de_last_move += 1

        return full_diagonal