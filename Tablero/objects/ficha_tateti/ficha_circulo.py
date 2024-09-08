from tablero.objects.ficha_tateti.tateti_object import TatetiObject

class FichaCirculo(TatetiObject):
    def __init__(self):
        super().__init__("circulo", "O", 3)
