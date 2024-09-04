import unittest

from tablero.casillero import Casillero
from tablero.objects.ficha_tateti.ficha_cruz import FichaCruz
from tablero.tablero_structure.tablero_structure import TableroStructure
from tablero.tablero_structure.casillero_structure.uniform_casillero_structure import UniformCasilleroStructure
from tablero.tablero_structure.piece_structure.uniform_piece_structure import UniformPieceStructure

class TestTablero(unittest.TestCase):
    def setUp(self):
        casillero_structure = UniformCasilleroStructure([Casillero])
        piece_structure = UniformPieceStructure([FichaCruz])
        self.tablero_structure = TableroStructure(casillero_structure, piece_structure, (3,3))

        self.casilleros_data = self.tablero_structure.crear_tablero()


    def test_01_casillero_structure(self):
        
        self.assertEqual(self.casilleros_data, "")