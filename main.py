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
from victory_checker.tateti_patterns.tateti_diagonal_right_left_checker import TatetiDiagonalLeftToRightChecker
from victory_checker.tateti_victory_checker import TatetiVictoryChecker


casillero_structure = UniformCasilleroStructure([Casillero])
piece_structure = UniformPieceStructure([FichaEmpty])
tablero_structure = TableroStructure(casillero_structure, piece_structure, (3,3))
tablero_printer = TableroPrinterConsola()
tateti_implementation = ConsoleImplementation()
teams = [TatetiTeam("Los Vateres", [TatetiPlayer("beto")], FichaCruz()), TatetiTeam("Los Inodoros", [TatetiPlayer("porky")], FichaCirculo())]
turno_manager = TeamOrientedTurnoManager(teams)

tablero = TableroLogica(tablero_printer, tablero_structure)

diagonal_checker = TatetiDiagonalLeftToRightChecker()
victory_checker = TatetiVictoryChecker([diagonal_checker], 3)

game = TatetiLogic(tateti_implementation, tablero, victory_checker, turno_manager, teams)
game.start_game()