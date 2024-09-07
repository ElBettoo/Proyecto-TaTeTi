from abc import ABC

class Player(ABC):
    def __init__(self, name):
        self.__name = name
    
    