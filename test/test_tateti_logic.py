import unittest
from unittest.mock import patch

from game_logic.tateti_implementation.console_implementation import ConsoleImplementation
from game_logic.tateti_logic import TatetiLogic
from player.tateti_player import TatetiPlayer
from tablero.casillero import Casillero
from tablero.objects.ficha_tateti.ficha_circulo import FichaCirculo
from tablero.objects.ficha_tateti.ficha_cruz import FichaCruz
from tablero.objects.ficha_tateti.ficha_empty import FichaEmpty
from tablero.tablero_logica import TableroLogica
from tablero.tablero_printer.tablero_printer_consola import TableroPrinterConsola
from tablero.tablero_structure.tablero_structure import TableroStructure
from tablero.tablero_structure.casillero_structure.uniform_casillero_structure import UniformCasilleroStructure
from tablero.tablero_structure.piece_structure.uniform_piece_structure import UniformPieceStructure
from team.tateti_team import TatetiTeam
from turno_manager.team_oriented_turno_manager import TeamOrientedTurnoManager
from victory_checker.tateti_patterns.tateti_diagonal_right_left_checker import TatetiDiagonalLeftToRightChecker
from victory_checker.tateti_victory_checker import TatetiVictoryChecker

class TestJuegoLogica(unittest.TestCase):
    def setUp(self):
        casillero_structure = UniformCasilleroStructure([Casillero])
        piece_structure = UniformPieceStructure([FichaEmpty])
        tablero_structure = TableroStructure(casillero_structure, piece_structure, (12,12))
        tablero_printer = TableroPrinterConsola()
        tateti_implementation = ConsoleImplementation()
        teams = [TatetiTeam("Los Vateres", [TatetiPlayer("beto")], FichaCruz), TatetiTeam("Los Inodoros", [TatetiPlayer("porky")], FichaCirculo)]
        turno_manager = TeamOrientedTurnoManager(teams)

        tablero = TableroLogica(tablero_printer, tablero_structure)

        diagonal_checker = TatetiDiagonalLeftToRightChecker()
        victory_checker = TatetiVictoryChecker([diagonal_checker], 4)

        self.game = TatetiLogic(tateti_implementation, tablero, victory_checker, turno_manager, teams)

    def test_01_constructor(self):
        self.assertEqual(self.casilleros_data, "")

    def test_02_input_tira_error_cuando_es_string(self):
        inputs = ["asdasdas", "1", 1, 2]
        with patch('builtins.input', side_effect=inputs) as mock_print: # Esto es para que se autocompleten los inputs en los test 
            self.game.start_game()
            mock_print.assert_called_with("Las cordenadas deben ser un numero")