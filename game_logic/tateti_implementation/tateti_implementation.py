from abc import ABC, abstractmethod

class TatetiImplementation(ABC):

    @abstractmethod
    def player_input(self):
        pass

    @abstractmethod
    def show_text(self):
        pass

    @abstractmethod
    def exit_game(self):
        exit()

    