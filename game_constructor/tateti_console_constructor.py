from game_constructor.game_constructor import GameConstructor
from game_logic.game_implementation.tateti_implementation.console_implementation import ConsoleImplementation
from game_logic.tateti_logic import TatetiLogic
from player.tateti_player import TatetiPlayer
from tablero.casillero import Casillero
from tablero.objects.ficha_tateti.ficha_circulo import FichaCirculo
from tablero.objects.ficha_tateti.ficha_cruz import FichaCruz
from tablero.objects.ficha_tateti.ficha_cuadrado import FichaCuadrado
from tablero.objects.ficha_tateti.ficha_empty import FichaEmpty
from tablero.tablero_logica import TableroLogica
from tablero.tablero_printer.tablero_printer_consola import TableroPrinterConsola
from tablero.tablero_structure.casillero_structure.uniform_casillero_structure import UniformCasilleroStructure
from tablero.tablero_structure.piece_structure.uniform_piece_structure import UniformPieceStructure
from tablero.tablero_structure.tablero_structure import TableroStructure
from team.tateti_team import TatetiTeam
from turno_manager.team_oriented_turno_manager import TeamOrientedTurnoManager
from victory_checker.tateti_patterns.tateti_column_checker import TatetiColumnChecker
from victory_checker.tateti_patterns.tateti_diagonal_left_right_checker import TatetiDiagonalRightToLeftChecker
from victory_checker.tateti_patterns.tateti_diagonal_right_left_checker import TatetiDiagonalLeftToRightChecker
from victory_checker.tateti_patterns.tateti_row_checker import TatetiRowChecker
from victory_checker.tateti_victory_checker import TatetiVictoryChecker

class TatetiConsoleConstructor(GameConstructor):
    def __init__(self):
        self.__implementation = ConsoleImplementation()
        self.__teams = []
        self.__TARGET_NAME = "config"
        self.__fichas_disponibles = [FichaCruz(), FichaCirculo(), FichaCuadrado()]
        self.__game: TatetiLogic = None

    def start_game(self):
        self.__game.start_game()

    def configure_game(self):
        teams = self.get_inputs()
        
        casillero_structure = UniformCasilleroStructure([Casillero])
        piece_structure = UniformPieceStructure([FichaEmpty])
        tablero_structure = TableroStructure(casillero_structure, piece_structure, (5,5))
        tablero_printer = TableroPrinterConsola()
        tablero = TableroLogica(tablero_printer, tablero_structure)

        tateti_implementation = ConsoleImplementation()

        turno_manager = TeamOrientedTurnoManager(teams)

        rl_diagonal_checker = TatetiDiagonalLeftToRightChecker()
        lr_diagonal_checker = TatetiDiagonalRightToLeftChecker()
        row_checker = TatetiRowChecker()
        column_checker = TatetiColumnChecker()
        victory_checker = TatetiVictoryChecker([rl_diagonal_checker, row_checker, column_checker, lr_diagonal_checker], 3)

        self.__game = TatetiLogic(tateti_implementation, tablero, victory_checker, turno_manager, teams)

    def get_inputs(self):
        cantidad_equipos = self.__get_int_input(f"Ingrese la cantidad de equipos [min=2] [max={len(self.__fichas_disponibles)}]", range(2,len(self.__fichas_disponibles)+1)) # max=3 elegido de manera arbitraria

        ficha_options = {number+1: f"{self.__fichas_disponibles[number].get_name().capitalize()} ['{self.__fichas_disponibles[number].get_simbolo()}']" for number in range(len(self.__fichas_disponibles))}
        for team in range(cantidad_equipos):

            self.__implementation.show_text("\n")
            team_name = self.__get_str_input("Ingrese el nombre del equipo [max_characters=15]", 15)

            ficha_menu = ""
            for key, value in ficha_options.items():
                ficha_menu += f"{key} - {value}\t"

            ficha_selected = self.__get_int_input(ficha_menu + "\nElije una ficha", ficha_options)
            ficha_options.pop(ficha_selected)

            cantidad_jugadores = self.__get_int_input(f"Ingrese la cantidad de jugadores del equipo ['{team_name}'] [max=5]", range(1,6)) # max=5 elegido de manera arbitraria
            player_list = []
            for jugador in range(cantidad_jugadores):
                player_name = self.__get_str_input(f"Ingrese el nombre del jugador [NRO°{jugador+1}] [max_characters=15]", 15)
                player_list.append(TatetiPlayer(player_name))
            
            team_instance = TatetiTeam(team_name, player_list, self.__fichas_disponibles[ficha_selected-1])
            self.__teams.append(team_instance)
        
        return self.__teams 




    def __get_str_input(self, input_message, max_len):
        input_state = False
        while not input_state:
            str_input = self.__implementation.get_input(input_message, self.__TARGET_NAME)

            if len(str_input) > max_len:
                self.__implementation.show_error("Se paso del maximo de caracteres permitidos")
            elif str_input == "":
                self.__implementation.show_error("Debe ingresar algo")
            else:
                input_state = True

        return str_input

    def __get_int_input(self, input_message, input_range):
        input_state = False
        while not input_state:
            int_input = self.__implementation.get_input(input_message, self.__TARGET_NAME)

            if not int_input.isnumeric():
                self.__implementation.show_error("Se debe ingresar un numero")
            elif int(int_input) not in input_range:
                self.__implementation.show_error("El numero no esta dentro del rango permitido")
            else:
                input_state = True

        return int(int_input)
