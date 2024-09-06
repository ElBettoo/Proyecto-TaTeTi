from tablero.casillero import Casillero
from tablero.tablero_logic import TableroLogica
from tablero.tablero_printer.tablero_printer_consola import TableroPrinterConsola
from tablero.objects.ficha_tateti.ficha_empty import FichaEmpty
from tablero.objects.ficha_tateti.ficha_cruz import FichaCruz
from tablero.tablero_structure.tablero_structure import TableroStructure
from tablero.tablero_structure.casillero_structure.uniform_casillero_structure import UniformCasilleroStructure
from tablero.tablero_structure.piece_structure.uniform_piece_structure import UniformPieceStructure

from victory_checker.tateti_victory_checker import TatetiVictoryChecker
from victory_checker.tateti_patterns.tateti_diagonal_right_left_checker import TatetiDiagonalLeftToRightChecker


class TatetiLogic():
    def __init__(self, tateti_implementation, tablero_logic):
        pass