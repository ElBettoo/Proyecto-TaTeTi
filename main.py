from game_logic.tateti_implementation.console_implementation import ConsoleImplementation
from game_logic.tateti_logic import TatetiLogic
from player.tateti_player import TatetiPlayer
from tablero.casillero import Casillero
from tablero.objects.ficha_tateti.ficha_circulo import FichaCirculo
from tablero.objects.ficha_tateti.ficha_cruz import FichaCruz
from tablero.objects.ficha_tateti.ficha_empty import FichaEmpty
from tablero.tablero_logica import TableroLogica
from tablero.tablero_printer.tablero_printer_consola import TableroPrinterConsola
from tablero.tablero_structure.casillero_structure.uniform_casillero_structure import UniformCasilleroStructure
from tablero.tablero_structure.piece_structure.uniform_piece_structure import UniformPieceStructure
from tablero.tablero_structure.tablero_structure import TableroStructure
from team.tateti_team import TatetiTeam
from turno_manager.team_oriented_turno_manager import TeamOrientedTurnoManager
from victory_checker.tateti_patterns.tateti_column_checker import TatetiColumnChecker
from victory_checker.tateti_patterns.tateti_diagonal_left_right_checker import TatetiDiagonalRightToLeftChecker
from victory_checker.tateti_patterns.tateti_diagonal_right_left_checker import TatetiDiagonalLeftToRightChecker
from victory_checker.tateti_patterns.tateti_row_checker import TatetiRowChecker
from victory_checker.tateti_victory_checker import TatetiVictoryChecker


casillero_structure = UniformCasilleroStructure([Casillero])
piece_structure = UniformPieceStructure([FichaEmpty])
tablero_structure = TableroStructure(casillero_structure, piece_structure, (5,5))
tablero_printer = TableroPrinterConsola()
tateti_implementation = ConsoleImplementation()
teams = [TatetiTeam("Los Vateres", [TatetiPlayer("beto")], FichaCruz()), TatetiTeam("Los Inodoros", [TatetiPlayer("porky")], FichaCirculo())]
turno_manager = TeamOrientedTurnoManager(teams)

tablero = TableroLogica(tablero_printer, tablero_structure)

rl_diagonal_checker = TatetiDiagonalLeftToRightChecker()
lr_diagonal_checker = TatetiDiagonalRightToLeftChecker()
row_checker = TatetiRowChecker()
column_checker = TatetiColumnChecker()
victory_checker = TatetiVictoryChecker([rl_diagonal_checker, row_checker, column_checker, lr_diagonal_checker], 3)

game = TatetiLogic(tateti_implementation, tablero, victory_checker, turno_manager, teams)
game.start_game()