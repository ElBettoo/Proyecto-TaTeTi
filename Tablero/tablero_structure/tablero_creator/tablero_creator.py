import random


from tablero.tablero_structure.casillero_bomba import CasilleroBomba

class TableroCreator: # Une el Casillero_Structure con Piece_Structure
    def __init__(self):
        self.__cantidad_bombas = 1

    def crear_tablero(self, casilleros_tablero, piezas_tablero, cantidad_casilleros):
        cantidad_columnas, cantidad_filas = cantidad_casilleros

        for row_cord in range(cantidad_filas):
            row_data = []
            for column_cord in range(cantidad_columnas):
                casilleros_tablero[row_cord][column_cord].change_piece(  new_piece=(piezas_tablero[row_cord][column_cord])  )

        for bomba in range(self.__cantidad_bombas):
            random_cord_x = random.randint(0,cantidad_columnas-1)
            random_cord_y = random.randint(0, cantidad_filas-1)
            casilleros_tablero[random_cord_y][random_cord_x] = CasilleroBomba(random_cord_y, random_cord_x, piezas_tablero[random_cord_y][random_cord_x])
        print(f"BOMBA PE: ({random_cord_x}, {random_cord_y})")
        
        return casilleros_tablero