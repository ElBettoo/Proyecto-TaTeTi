from tablero.objects.ficha_tateti.tateti_object import TatetiObject
from dataclasses import dataclass

@dataclass
class FichaEmpty(TatetiObject):
    __name: str = "empty"
    __simbolo: str = " "

    @property
    def simbolo(self):
        return self.__simbolo

    @property
    def name(self):
        return self.__name