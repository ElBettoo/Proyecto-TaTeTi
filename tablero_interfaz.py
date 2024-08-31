from abc import ABC, abstractmethod
from tablero_printer_interfaz import TableroPrinterInterfaz

class TableroInterfaz(ABC): # tener metodo para pedir data. no hace falta interfaz 
    def __init__(self, tablero_printer: TableroPrinterInterfaz, cantidad_casilleros: int):
        self.__tablero_printer = tablero_printer
        self.__cantidad_casilleros = cantidad_casilleros
        self.__CASILLERO_VACIO = "_"
        self.__casilleros_data = self.__crear_casillero_data(cantidad_casilleros)
        

    def __crear_casillero_data(self, cantidad_casilleros: int):
        casilleros_data = []

        for row in range(cantidad_casilleros):
            row_data = []
            for column in range(cantidad_casilleros):
                casillero = self.__CASILLERO_VACIO
                row_data.append(casillero)

            casilleros_data.append(row_data)

        return casilleros_data

    def imprimir(self):
        return self.__tablero_printer.dibujar_tablero(self.__casilleros_data)

    def poner_ficha(self, pos_x, pos_y, ficha):
        self.__casilleros_data[pos_y][pos_x] = ficha
        
