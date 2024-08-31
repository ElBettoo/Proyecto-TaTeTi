from abc import ABC, abstractmethod

class TableroPrinterInterfaz(ABC):
    @abstractmethod
    def dibujar_tablero(self, casilleros_data: list[list[str]]):
        pass