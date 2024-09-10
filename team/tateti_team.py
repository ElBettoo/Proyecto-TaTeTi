from team.teams import Team
from player.player import Player
from tablero.objects.ficha_tateti.tateti_object import TatetiObject

class TatetiTeam(Team):
    def __init__(self, name, players: list[Player], ficha: TatetiObject):
        super().__init__(name, players)
        self.__name = name
        self.__players = players
        self.__ficha = ficha # No es una instancia. Es una clase 
