from abc import ABC, abstractmethod
from game_logic.game_logic import GameLogic

class GameConstructor(ABC):
    def __init__(self):
        self.__game: GameLogic
    
    @abstractmethod
    def configure_game(self) -> GameLogic:
        pass

    @abstractmethod
    def start_game(self):
        pass
