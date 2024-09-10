from abc import ABC, abstractmethod

class GameImplementation(ABC):
    @abstractmethod
    def get_input(self):
        pass

    @abstractmethod
    def show_text(self):
        pass