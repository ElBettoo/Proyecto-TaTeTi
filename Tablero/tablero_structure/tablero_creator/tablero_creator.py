

class TableroCreator: # Une el Casillero_Structure con Piece_Structure

    def crear_tablero(self, casilleros_tablero, piezas_tablero, cantidad_casilleros):
        cantidad_columnas, cantidad_filas = cantidad_casilleros

        for row_cord in range(cantidad_filas):
            row_data = []
            for column_cord in range(cantidad_columnas):
                casilleros_tablero[row_cord][column_cord].change_piece(  new_piece=(piezas_tablero[row_cord][column_cord])  )
        
        return casilleros_tablero