from game_logic.tateti_implementation.console_implementation import ConsoleImplementation
from player.tateti_player import TatetiPlayer
from tablero.casillero import Casillero
from tablero.tablero_logica import TableroLogica
from tablero.tablero_printer.tablero_printer_consola import TableroPrinterConsola
from tablero.objects.ficha_tateti.ficha_empty import FichaEmpty
from tablero.objects.ficha_tateti.ficha_cruz import FichaCruz
from tablero.objects.ficha_tateti.ficha_circulo import FichaCirculo
from tablero.tablero_structure.tablero_structure import TableroStructure
from tablero.tablero_structure.casillero_structure.uniform_casillero_structure import UniformCasilleroStructure
from tablero.tablero_structure.piece_structure.uniform_piece_structure import UniformPieceStructure

from game_logic.tateti_implementation.tateti_implementation import TatetiImplementation
from team.tateti_team import TatetiTeam
from turno_manager.team_oriented_turno_manager import TeamOrientedTurnoManager
from turno_manager.turno_manager import TurnoManager
from victory_checker.tateti_victory_checker import TatetiVictoryChecker
from victory_checker.tateti_patterns.tateti_diagonal_right_left_checker import TatetiDiagonalLeftToRightChecker


class TatetiLogic():
    def __init__(self, tateti_implementation: TatetiImplementation, tablero_logica: TableroLogica, victory_checker: TatetiVictoryChecker, turno_manager: TurnoManager, teams: list[TatetiTeam]):
        self.__implementation = tateti_implementation
        self.__tablero = tablero_logica
        self.__victory_checker = victory_checker
        self.__turno_manager = turno_manager
        self.__teams = teams

    def start_game(self):
        someone_won = False
        while not someone_won:
            self.show_text(self.__tablero.imprimir())

            current_player = self.__turno_manager.get_player_turn()
            current_team = self.__turno_manager.get_team_turn()

            input_state = False
            while not input_state:
                try: 
                    pos_x = int(self.get_player_input(f"Ingrese la fila donde quiere colocar la ficha ['{current_team._TatetiTeam__ficha.get_simbolo()}']", current_player)) - 1
                    pos_y = int(self.get_player_input(f"Ingrese la columna donde quiere colocar la ficha ['{current_team._TatetiTeam__ficha.get_simbolo()}']", current_player)) - 1 # -1 por que el indice arranca de 0
                except ValueError:
                    self.show_error("Las cordenadas deben ser un numero")
                    continue
                
                input_data = self.cords_are_valid((pos_x, pos_y)) # Devuelve un dict con 'condition' y 'message' como keys

                input_state = input_data["condition"]
                if not input_state:
                    self.show_error(input_data["message"])

            self.__tablero.change_piece((pos_x, pos_y), current_team._TatetiTeam__ficha.create_new_ficha())
            self.__turno_manager.next_turn()
            someone_won = self.__victory_checker.check_win(self.__tablero._TableroLogica__tablero_structure, (pos_x, pos_y))
        
        self.show_text(self.__tablero.imprimir())
        self.show_win(f"Gano el equipo '{current_team._TatetiTeam__name}'")

    def cords_are_valid(self, cords: tuple[int, int]) -> bool:
        return self.__tablero.cords_validator(cords)

    def get_player_input(self, input_message, player):
        return self.__implementation.get_input(input_message, player._TatetiPlayer__name)
    
    def show_text(self, text):
        return self.__implementation.show_text(text)
    
    def show_error(self, text):
        return self.__implementation.show_error(text)
    
    def show_win(self, text):
        return self.__implementation.show_win(text)