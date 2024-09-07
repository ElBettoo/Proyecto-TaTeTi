from player.player import Player

class TatetiPlayer(Player):
    def __init__(self, name):
        super().__init__()
        self.__name = name

    def poner_ficha(self, ficha, cordenada):
        return f"[{self.__name}]: Coloco la ficha {ficha} en la cordenada {cordenada}" # No necesidad de esta funcion para el juego TATETI