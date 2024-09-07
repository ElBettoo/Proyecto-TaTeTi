from team.teams import Team
from player.player import Player

class SimpleTeam(Team):
    def __init__(self, name, players: list[Player]):
        super().__init__()
        self.__name = name
        self.__players = players
        self.__points: int = 0
    
    def add_points(self, points):
        self.__points += points
    
