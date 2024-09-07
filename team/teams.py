from abc import ABC
from player.player import Player

class Team(ABC):
    def __init__(self, name, players: list[Player]):
        self.__jugadores = players
        self.__name = name
        self.__points = 0

    def __getitem__(self, index):
        return self.__jugadores[index]
    
    def __len__(self):
        return len(self.__jugadores)
    