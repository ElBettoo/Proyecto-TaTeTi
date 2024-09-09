from abc import ABC, abstractmethod

class TatetiImplementation(ABC):

    @abstractmethod
    def get_input(self):
        pass

    @abstractmethod
    def show_text(self):
        pass

    @abstractmethod
    def show_error(self):
        pass

    @abstractmethod
    def show_win(self):
        pass

    @abstractmethod
    def exit_game(self):
        exit()

    