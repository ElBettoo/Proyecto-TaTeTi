from tablero.objects.ficha_tateti.tateti_object import TatetiObject

class FichaCuadrado(TatetiObject):
    def __init__(self):
        super().__init__("cuadrado", "▢", 4)
