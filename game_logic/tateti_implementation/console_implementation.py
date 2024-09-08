from game_logic.tateti_implementation.tateti_implementation import TatetiImplementation

class ConsoleImplementation(TatetiImplementation):
    def __init__(self):
        self.__commands = {"exit", "endgame"}

    def player_input(self, player_name, input_message: str):
        return input(f"[{player_name}]: {input_message}\n: ")
    
    def show_text(self, text):
        print(text + "\n")

    def exit_game(self):
        return super().exit_game()