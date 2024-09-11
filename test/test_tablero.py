import unittest

from tablero.objects.ficha_tateti.ficha_empty import FichaEmpty
from tablero.tablero_logica import TableroLogica
from tablero.tablero_printer.tablero_printer_interfaz import TableroPrinterInterfaz
from tablero.tablero_structure.casillero import Casillero
from tablero.objects.ficha_tateti.ficha_cruz import FichaCruz
from tablero.tablero_structure.tablero_structure import TableroStructure
from tablero.tablero_structure.casillero_structure.uniform_casillero_structure import UniformCasilleroStructure
from tablero.tablero_structure.piece_structure.uniform_piece_structure import UniformPieceStructure

class TestTablero(unittest.TestCase):
    def setUp(self):
        self.casillero_structure = UniformCasilleroStructure([Casillero])
        self.piece_structure = UniformPieceStructure([FichaEmpty])
        self.tablero_structure = TableroStructure(self.casillero_structure, self.piece_structure, (3,3))

        self.casilleros_data = self.tablero_structure.crear_tablero()

        self.tablero = TableroLogica(TableroPrinterInterfaz,self.tablero_structure)

    def test_01_todo_tablero_ocupado_devuelve_true_cuando_esta_completo(self):
        piece_structure = UniformPieceStructure([FichaCruz])
        tablero_structure = TableroStructure(self.casillero_structure, piece_structure, (3,3))
        tablero = TableroLogica(TableroPrinterInterfaz,tablero_structure)
        self.assertTrue(tablero.is_todo_tablero_ocupado())

    def test_02_todo_tablero_ocupado_devuelve_false_cuando_esta_incompleto(self):
        self.tablero.change_piece((1,1),FichaCruz)
        self.assertTrue(not self.tablero.is_todo_tablero_ocupado())