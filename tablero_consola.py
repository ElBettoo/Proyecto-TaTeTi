from tablero_interfaz import TableroInterfaz
from tablero_printer_interfaz import TableroPrinterInterfaz

class TableroConsola(TableroInterfaz):
    def __init__(self, tablero_printer: TableroPrinterInterfaz, cantidad_casilleros: int):
        super().__init__(tablero_printer, cantidad_casilleros)
        print(self.__casilleros_data)
        print(self.__CASILLERO_VACIO)

tablero = TableroConsola("ac", 3)