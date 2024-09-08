from tablero.objects.ficha_tateti.tateti_object import TatetiObject

class FichaCruz(TatetiObject):
    def __init__(self):
        super().__init__("cruz", "X", 1)