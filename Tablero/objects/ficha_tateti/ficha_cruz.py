from tablero.objects.ficha_tateti.tateti_object import TatetiObject
from dataclasses import dataclass

@dataclass
class FichaCruz(TatetiObject):
    __name: str = "Cruz"
    __simbolo: str = "X"

    @property
    def simbolo(self):
        return self.__simbolo

    @property
    def name(self):
        return self.__name