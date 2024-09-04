from tablero.objects.ficha_tateti.tateti_object import TatetiObject
from dataclasses import dataclass

@dataclass
class FichaCirculo(TatetiObject):
    __name: str = "Circulo"
    __simbolo: str = "O"

    @property
    def simbolo(self):
        return self.__simbolo

    @property
    def name(self):
        return self.__name