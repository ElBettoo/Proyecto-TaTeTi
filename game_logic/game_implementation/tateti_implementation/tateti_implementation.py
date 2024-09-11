from abc import ABC, abstractmethod
from game_logic.game_implementation.game_implementation import GameImplementation

class TatetiImplementation(GameImplementation):
    @abstractmethod
    def show_error(self):
        pass

    @abstractmethod
    def show_win(self):
        pass

    @abstractmethod
    def show_empate(self):
        pass

    @abstractmethod
    def exit_game(self):
        exit()

    