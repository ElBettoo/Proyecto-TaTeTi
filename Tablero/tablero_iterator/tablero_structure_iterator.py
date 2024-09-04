from collections.abc import Iterator


class TableroStructureIterator(Iterator):
    def __init__(self, casilleros_data: list[list]):
        self.__casilleros_data = casilleros_data
        self.__indice_x = 0
        self.__indice_y = 0

    def __next__(self):
        if self.__indice_y >= len(self.__casilleros_data):
            raise StopIteration

        fila_entera = [casillero.piece.simbolo for casillero in self.__casilleros_data[self.__indice_y][:]]
        self.__indice_y += 1
        return fila_entera
        

        