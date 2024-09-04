from abc import ABC, abstractmethod
from tablero.casillero import Casillero
from tablero.tablero_structure.tablero_structure import TableroStructure

class TableroPrinterInterfaz(ABC):
    @abstractmethod
    def dibujar_tablero(self, tablero_structure: TableroStructure):
        pass