from abc import ABC, abstractmethod

class PieceStructure(ABC):
    def __init__(self):
        self.__starting_position = list
        self.__always_compatible = bool

    @abstractmethod
    def check_compatibility(self, cantidad_casilleros: tuple[int, int]):
        pass

    @abstractmethod
    def get_starting_pieces(self, cantidad_casilleros: tuple[int, int]):
        pass