from tablero.tablero_printer.tablero_printer_interfaz import TableroPrinterInterfaz
from tablero.tablero_structure.tablero_structure import TableroStructure
from tablero.objects.tablero_object import TableroObject
from tablero.casillero import Casillero

class TableroLogica(): # tener metodo para pedir data. no hace falta interfaz 
    def __init__(self, tablero_printer: TableroPrinterInterfaz, tablero_structure: TableroStructure): 
        self.__tablero_printer = tablero_printer
        self.__tablero_structure = tablero_structure

    def imprimir(self) -> str:
        return self.__tablero_printer.dibujar_tablero(self.__tablero_structure)

    def change_piece(self, cords: tuple(int, int), new_object: TableroObject):
        pos_x, pos_y = cords
        casillero = self.casilleros_data[pos_y][pos_x]
        casillero.change_piece(new_object)

    def get_casillero_by_cords(self, cords: tuple(int, int)) -> TableroObject:
        pos_x, pos_y = cords
        return self.casilleros_data[pos_y][pos_x]

    @property
    def casilleros_data(self):
        return self.__tablero_structure.casilleros_data        
