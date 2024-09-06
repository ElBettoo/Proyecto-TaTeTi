from tateti_implementation import TatetiImplementation

class ConsoleImplementation(TatetiImplementation):
    def player_input(self, input_message, player):
        return f"[{player.name}]: {input_message}"
    
    def show_text(self, text):
        print(text)