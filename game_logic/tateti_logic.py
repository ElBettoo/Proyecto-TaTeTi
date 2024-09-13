import time
from tablero.tablero_logica import TableroLogica
from game_logic.game_implementation.tateti_implementation.tateti_implementation import TatetiImplementation
from team.tateti_team import TatetiTeam
from turno_manager.turno_manager import TurnoManager
from victory_checker.tateti_victory_checker import TatetiVictoryChecker


class TatetiLogic():
    def __init__(self, tateti_implementation: TatetiImplementation, tablero_logica: TableroLogica, victory_checker: TatetiVictoryChecker, turno_manager: TurnoManager, teams: list[TatetiTeam]):
        self.__implementation = tateti_implementation
        self.__tablero = tablero_logica
        self.__victory_checker = victory_checker
        self.__turno_manager = turno_manager
        self.__teams = teams

    def start_game(self):
        someone_won = False
        empate = False
        while not someone_won and not empate:
            self.show_text(self.__tablero.imprimir())

            current_player = self.__turno_manager.get_player_turn()
            current_team = self.__turno_manager.get_team_turn()

            input_state = False
            while not input_state:
                try: 
                    pos_x = int(self.get_player_input(f"Ingrese la columna donde quiere colocar la ficha ['{current_team._TatetiTeam__ficha.get_simbolo()}']", current_player)) - 1 # -1 por que el indice arranca de 0
                    pos_y = int(self.get_player_input(f"Ingrese la fila donde quiere colocar la ficha ['{current_team._TatetiTeam__ficha.get_simbolo()}']", current_player)) - 1
                except ValueError:
                    self.show_error("Las cordenadas deben ser un numero")
                    continue
                
                input_data = self.cords_are_valid((pos_x, pos_y)) # Devuelve un dict con 'condition' y 'message' como keys

                input_state = input_data["condition"]
                if not input_state:
                    self.show_error(input_data["message"])

            self.__turno_manager.next_turn()

            if self.__tablero.is_casillero_bomba((pos_x, pos_y)):
                casillero_bomba = self.__tablero.get_casillero_by_cords((pos_x, pos_y))
                if casillero_bomba._CasilleroBomba__active:
                    casillero_bomba._CasilleroBomba__active = False
                    self.show_text(f"El jugador [{current_player._TatetiPlayer__name}] puso una ficha en una bomba, !Que mala suerte!")
                    time.sleep(.5)
                    continue

            self.__tablero.change_piece((pos_x, pos_y), current_team._TatetiTeam__ficha.create_new_ficha())
            someone_won = self.__victory_checker.check_win(self.__tablero._TableroLogica__tablero_structure, (pos_x, pos_y))
            empate = self.__tablero.is_todo_tablero_ocupado()


            
        
        if someone_won:
            self.show_text(self.__tablero.imprimir())
            self.show_win(f"Gano el equipo '{current_team._TatetiTeam__name}'")
        else:
            self.show_text(self.__tablero.imprimir())
            self.show_empate("Se llego a un empate")            

    def cords_are_valid(self, cords: tuple[int, int]) -> bool:
        return self.__tablero.cords_validator(cords)

    def get_player_input(self, input_message, player):
        return self.__implementation.get_input(input_message, player._TatetiPlayer__name)
    
    def show_text(self, text):
        return self.__implementation.show_text(text)
    
    def show_empate(self, text):
        return self.__implementation.show_empate(text)
    
    def show_error(self, text):
        return self.__implementation.show_error(text)
    
    def show_win(self, text):
        return self.__implementation.show_win(text)