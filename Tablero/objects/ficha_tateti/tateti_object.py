from tablero.objects.tablero_object import TableroObject

class TatetiObject(TableroObject):
    def __init__(self, name: str, simbolo: str, color: int = 9):
        self.__name = name
        self.__simbolo = simbolo
        self.__color = color # number from 0 to 9. '\033[{self.__color}4m' for color

    def __eq__(self, otro):
        if not isinstance(otro, TatetiObject):
            raise ValueError("Se esta comparando un 'TatetiObject' con otro elemento desconocido")
        return self.__simbolo == otro.__simbolo
    
    def get_simbolo(self):
        return f'\033[3{self.__color}m' + self.__simbolo + '\033[39m'
    
    def create_new_ficha(self): # Wrong?. patron de diseño Factory?
        instance_class = self.__class__
        return instance_class()