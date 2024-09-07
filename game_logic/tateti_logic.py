from tablero.casillero import Casillero
from tablero.tablero_logic import TableroLogica
from tablero.tablero_printer.tablero_printer_consola import TableroPrinterConsola
from tablero.objects.ficha_tateti.ficha_empty import FichaEmpty
from tablero.objects.ficha_tateti.ficha_cruz import FichaCruz
from tablero.tablero_structure.tablero_structure import TableroStructure
from tablero.tablero_structure.casillero_structure.uniform_casillero_structure import UniformCasilleroStructure
from tablero.tablero_structure.piece_structure.uniform_piece_structure import UniformPieceStructure

from game_logic.tateti_implementation.tateti_implementation import TatetiImplementation
from team.teams import Team
from turno_manager.turno_manager import TurnoManager
from victory_checker.tateti_victory_checker import TatetiVictoryChecker
from victory_checker.tateti_patterns.tateti_diagonal_right_left_checker import TatetiDiagonalLeftToRightChecker


class TatetiLogic():
    def __init__(self, tateti_implementation: TatetiImplementation, tablero_logica: TableroLogica, victory_checker: TatetiVictoryChecker, turno_manager: TurnoManager, teams: list[Team]):
        self.__implementation = tateti_implementation
        self.__tablero = tablero_logica
        self.__victory_checker = victory_checker
        self.__turno_manager = turno_manager
        self.__teams = teams

    def start_game(self):
        pass

    def restart_game(self):
        pass

    def exit_game(self):
        exit()

    def get_player_input(self, input_message, player):
        return self.__implementation.player_input(player, input_message)

    def show_text(self, text):
        return self.__implementation.show_text(text)