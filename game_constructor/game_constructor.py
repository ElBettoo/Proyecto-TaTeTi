from abc import ABC, abstractmethod

class GameConstructor(ABC):
    @abstractmethod
    def configure_game(self):
        pass

    @abstractmethod
    def start_game(self):
        pass

    @abstractmethod
    def get_inputs(self):
        pass
