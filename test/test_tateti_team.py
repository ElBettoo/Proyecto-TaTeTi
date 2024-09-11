import unittest

from player.tateti_player import TatetiPlayer
from tablero.objects.ficha_tateti.ficha_cruz import FichaCruz
from team.tateti_team import TatetiTeam

class TestTeam(unittest.TestCase):
    def setUp(self):
        name = "beto team"
        self.players = [TatetiPlayer("beto")]
        ficha = FichaCruz()
        self.team = TatetiTeam(name, self.players, ficha)

    def test_01_constructor(self):
        self.assertTrue(isinstance(self.team, TatetiTeam))

    def test_02_get_item_by_index(self):
        player_0 = self.team[0]
        self.assertEqual(player_0, self.players[0])

    def test_03_team_len(self):
        len_value = len(self.team)
        self.assertEqual(len_value, 1)