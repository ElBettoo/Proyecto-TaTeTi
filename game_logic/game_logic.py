from abc import ABC, abstractmethod
from game_logic.game_implementation.game_implementation import GameImplementation

class GameLogic(ABC):
    def __init__(self, implementation: GameImplementation):
        self.__implementation = implementation

    @abstractmethod
    def start_game():
        pass