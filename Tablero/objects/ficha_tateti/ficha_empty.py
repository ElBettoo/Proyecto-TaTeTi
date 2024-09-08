from tablero.objects.empty_object import EmptyObject
from tablero.objects.ficha_tateti.tateti_object import TatetiObject

class FichaEmpty(TatetiObject, EmptyObject):
    def __init__(self):
        super().__init__("empty", " ")