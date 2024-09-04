from tablero.casillero import Casillero
from tablero.objects.ficha_tateti.ficha_empty import FichaEmpty
from tablero.tablero_structure.tablero_structure import TableroStructure
from tablero.tablero_structure.casillero_structure.uniform_casillero_structure import UniformCasilleroStructure
from tablero.tablero_structure.piece_structure.uniform_piece_structure import UniformPieceStructure


if __name__ == '__main__':
    casillero_structure = UniformCasilleroStructure([Casillero])
    piece_structure = UniformPieceStructure([FichaEmpty])
    tablero_structure = TableroStructure(casillero_structure, piece_structure, (32,32))

    cantidad_filas, cantidad_columnas = tablero_structure.cantidad_casilleros
    space = "  "
    separator = "|"
    x_cords_str = " " * int( (len(space) * 2))
    print(f"{space}{space}  {" " * int(len(x_cords_str) / 2)}" + (x_cords_str).join(str(num+1).zfill(2) for num in range(cantidad_columnas)))  
    print(f"{space}{space}  +" + (("-" * (len(space) * 2 + 1)) + "+") * cantidad_columnas) # +1 por el simbolo cruz/circulo
    for row_idx, row in enumerate(tablero_structure):
        cords_str = str(row_idx+1).zfill(2)
        casilleros_str = f"{space}{separator}{space}".join(str(tupla) for tupla in row) 


        row_str =  f"{cords_str}{space}{space}{separator}{space}{casilleros_str}{space}{separator}"

        column_len = int((len(row_str) - (len(space) * 2) - 4 - (cantidad_columnas - 1)) / cantidad_columnas) # -1 por el numero index.   len(row)-1 por los '+' repetidos sin contar lo del borde

        print(row_str)
        print(f"  {space}{space}" + "+" + (("-" * column_len) + "+") * len(row))
    
    """
    casilleros_data = tablero_structure.casilleros_data

    for row in casilleros_data:
        for casillero in row: 
            print(casillero.get_cords(), end=" ")
        print("")
    """