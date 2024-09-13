from tablero.tablero_structure.tablero_structure import TableroStructure
from victory_checker.tateti_patterns.tateti_victory_pattern import TatetiVictoryPattern
from victory_checker.victory_checker import VictoryChecker
from tablero.objects.ficha_tateti.ficha_empty import FichaEmpty

class TatetiVictoryChecker(VictoryChecker):
    def __init__(self, victory_patterns: list[TatetiVictoryPattern], win_length: tuple[int, int]):
        self.__victory_patterns = victory_patterns
        self.__win_length = win_length

    def check_win(self, tablero_structure: TableroStructure, last_move: tuple[int, int]):
        return self.check_all_combinations(tablero_structure, last_move)
    
    def check_all_combinations(self, tablero_structure: TableroStructure, last_move: tuple[int, int]):
        for pattern in self.__victory_patterns:
            possible_cords, win_length = pattern.get_possible_cords_by_last_move(tablero_structure.cantidad_casilleros, last_move, self.__win_length)
            if self.__check_combinations(tablero_structure, possible_cords, win_length):
                return True
        return False

    def __check_combinations(self, tablero_structure: TableroStructure, possible_cords, win_length):
        tablero = tablero_structure.casilleros_data

        for combination in possible_cords:
            all_possible_cords = combination     
            print(f"combination: {combination}   possible_cords: {possible_cords}")   
            #  Todas las posiciones/coordenadas de la diagonal - Posiciones necesarias para ganar. Si no hay suficientes posiciones en la diagonal para poder ganar, no se ejecuta, da 0
            spaces_for_win = max(0,  len(all_possible_cords) - (win_length - 1)) # len(all_possible_cords) - (win_length - 1) = Cuantas veces entre la cantidad de fichas para ganar en las cordenadas posibles
            index = 0

            for possible_win in range(spaces_for_win): # Esto calcula todas las combinaciones posibles en base a todos los valores de la diagonal 
                combination = []
                
                for ficha_pos in range(win_length):
                    pos_x, pos_y = all_possible_cords[ficha_pos + index]
                    combination.append(tablero[pos_y][pos_x])
                index += 1

                if all(casillero.piece == combination[0].piece for casillero in combination) and not isinstance(combination[0].piece, FichaEmpty):
                        return True
        
        return False
 