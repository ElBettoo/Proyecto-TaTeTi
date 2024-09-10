from tablero.tablero_printer.tablero_printer_interfaz import TableroPrinterInterfaz
from tablero.tablero_structure.tablero_structure import TableroStructure
from tablero.tablero_structure.casillero import Casillero

class TableroPrinterConsola(TableroPrinterInterfaz):
    def __init__(self):
        self.__tablero_str = ""

    def __add_new_str_line(self, new_line):
        self.__tablero_str = self.__tablero_str + "\n" + new_line

    def __reset_tablero_str(self):
        self.__tablero_str = ""

    def dibujar_tablero(self, tablero_structure: TableroStructure):
        
        cantidad_filas, cantidad_columnas = tablero_structure.cantidad_casilleros
        space = "  "
        separator = "|"
        x_cords_str = " " * int( (len(space) * 2))
        padding = " " * int(len(x_cords_str) / 2)
        self.__add_new_str_line(f"{space}{space}  {padding}" + (x_cords_str).join(str(num+1).zfill(2) for num in range(cantidad_columnas)))  
        self.__add_new_str_line(f"{space}{space}  +" + (("-" * (len(space) * 2 + 1)) + "+") * cantidad_columnas) # +1 por el simbolo cruz/circulo
        for row_idx, row in enumerate(tablero_structure):
            cords_str = str(row_idx+1).zfill(2)
            casilleros_str = f"{space}{separator}{space}".join(str(tupla) for tupla in row) 


            row_str =  f"{cords_str}{space}{space}{separator}{space}{casilleros_str}{space}{separator}"

            column_len = int(((len(row_str) - (len(space) * 2) - 4 - (cantidad_columnas - 1)) / cantidad_columnas) - 10) # -4 por el numero index.   len(row)-1 por los '+' repetidos sin contar lo del borde -10 por el color format

            self.__add_new_str_line(row_str)
            self.__add_new_str_line(f"  {space}{space}" + "+" + (("-" * column_len) + "+") * len(row))

        tablero_str = self.__tablero_str
        self.__reset_tablero_str()
        return tablero_str