from tablero.tablero_printer.tablero_printer_interfaz import TableroPrinterInterfaz
from tablero.tablero_structure.tablero_structure import TableroStructure
from tablero.casillero import Casillero

class TableroPrinterConsola(TableroPrinterInterfaz):

    def dibujar_tablero(self, tablero_structure: TableroStructure):
        
        cantidad_filas, cantidad_columnas = tablero_structure.cantidad_casilleros
        space = "  "
        separator = "|"
        print(space * 2, (num+1 for num in range(cantidad_columnas)))
        print(f"{space}{space} +" + ("-" * (len(space) * 2 + 6)) + "+") # +1 por el simbolo cruz/circulo
        for row_idx, row in enumerate(tablero_structure):
            cords_str = f"{row_idx}"
            casilleros_str = f"{space}{separator}{space}".join(str(tupla) for tupla in row) 


            row_str =  f"{cords_str}{space}{space}{separator}{space}{casilleros_str}{space}{separator}"

            column_len = int((len(row_str) - (len(space) * 2) - 1 - (len(row) - 1)) / len(row)) # -1 por el numero index.   len(row)-1 por los '+' repetidos sin contar lo del borde

            print(row_str)
            print(f" {space}{space}" + "+" + (("-" * column_len) + "+") * len(row))