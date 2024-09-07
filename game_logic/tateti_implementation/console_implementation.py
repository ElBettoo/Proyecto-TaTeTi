from game_logic.tateti_implementation.tateti_implementation import TatetiImplementation

class ConsoleImplementation(TatetiImplementation):
    def __init__(self):
        self.__commands = {"exit", "endgame"}

    def player_input(self, player, input_message: str):
        return f"[{player.__name}] {input_message}\n: "
    
    def show_text(self, text):
        print(text)