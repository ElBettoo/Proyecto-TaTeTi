import unittest

from tablero.casillero import Casillero
from tablero.objects.ficha_tateti.ficha_cruz import FichaCruz
from tablero.objects.ficha_tateti.ficha_empty import FichaEmpty
from tablero.tablero_logic import TableroLogica
from tablero.tablero_printer.tablero_printer_consola import TableroPrinterConsola
from tablero.tablero_structure.tablero_structure import TableroStructure
from tablero.tablero_structure.casillero_structure.uniform_casillero_structure import UniformCasilleroStructure
from tablero.tablero_structure.piece_structure.uniform_piece_structure import UniformPieceStructure
from victory_checker.tateti_patterns.tateti_diagonal_right_left_checker import TatetiDiagonalLeftToRightChecker
from victory_checker.tateti_victory_checker import TatetiVictoryChecker

class TestJuegoLogica(unittest.TestCase):
    def setUp(self):
        casillero_structure = UniformCasilleroStructure([Casillero])
        piece_structure = UniformPieceStructure([FichaEmpty])
        tablero_structure = TableroStructure(casillero_structure, piece_structure, (12,12))
        tablero_printer = TableroPrinterConsola()

        tablero = TableroLogica(tablero_printer, tablero_structure)

        diagonal_checker = TatetiDiagonalLeftToRightChecker()
        victory_checker = TatetiVictoryChecker([diagonal_checker], 4)

    def test_01_constructor(self):
        
        self.assertEqual(self.casilleros_data, "")