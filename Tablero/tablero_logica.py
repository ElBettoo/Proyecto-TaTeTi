from tablero.tablero_printer.tablero_printer_interfaz import TableroPrinterInterfaz
from tablero.tablero_structure.tablero_structure import TableroStructure
from tablero.objects.tablero_object import TableroObject
from tablero.objects.empty_object import EmptyObject

class TableroLogica(): # tener metodo para pedir data. no hace falta interfaz 
    def __init__(self, tablero_printer: TableroPrinterInterfaz, tablero_structure: TableroStructure): 
        self.__tablero_printer = tablero_printer
        self.__tablero_structure = tablero_structure

    def imprimir(self) -> str:
        return self.__tablero_printer.dibujar_tablero(self.__tablero_structure)

    def change_piece(self, cords: tuple[int, int], new_object: TableroObject):
        pos_x, pos_y = cords
        casillero = self.casilleros_data[pos_y][pos_x]
        casillero.change_piece(new_object)

    def get_casillero_by_cords(self, cords: tuple[int, int]) -> TableroObject:
        pos_x, pos_y = cords
        return self.casilleros_data[pos_y][pos_x]
    
    def is_todo_tablero_ocupado(self) -> bool:
        casilleros_data = self.__tablero_structure.casilleros_data
        for row in casilleros_data:
            for casillero in row:
                if not self.is_casillero_ocupado(casillero.get_cords()):
                    return False
        return True 
    
    def is_casillero_ocupado(self, cords: tuple[int, int]):
        casillero = self.get_casillero_by_cords(cords)
        return not isinstance(casillero.piece, EmptyObject)
    
    def cords_validator(self, cords: tuple[int, int]):
        pos_x, pos_y = cords
        cords_data = {"condition": True, "message": "Cordenadas validas"}

        cant_x, cant_y = self.__tablero_structure.cantidad_casilleros
        if (pos_x+1 > cant_x) or (pos_y+1 > cant_y) or (pos_x < 0) or (pos_y < 0): # Si es negativo o mayor a la cantidad de filas/columnas
            cords_data["condition"] = False
            cords_data["message"] = "Cordenadas fuera del rango del tablero"
            return cords_data

        if self.is_casillero_ocupado(cords):
            cords_data["condition"] = False
            cords_data["message"] = "El casillero esta ocupado"
 
        return cords_data
    
    @property
    def casilleros_data(self):
        return self.__tablero_structure.casilleros_data        
