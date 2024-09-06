from tablero.objects.tablero_object import TableroObject

class TatetiObject(TableroObject):
    def __init__(self):
        self.__name = str
        self.__simbolo = str

    def __eq__(self, otro):
        if not isinstance(otro, TatetiObject):
            raise Exception("Error")
        return self.__simbolo == otro.__simbolo