from abc import ABC, abstractmethod
from team.teams import Team

class TurnoManager(ABC):
    def __init__(self, teams: list[Team]):
        self.__teams = teams
        self.__team_index = 0
        self.__player_index = 0

    @abstractmethod
    def get_player_turn(self):
        pass

    @abstractmethod
    def get_team_turn(self):
        pass

    @abstractmethod
    def next_turn(self):
        pass