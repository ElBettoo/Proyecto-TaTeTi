from game_logic.game_implementation.tateti_implementation.tateti_implementation import TatetiImplementation

class ConsoleImplementation(TatetiImplementation):
    def __init__(self):
        self.__target_color = 3
        self.__win_color = 2
        self.__empate_color = 3
        self.__error_color = 1

    def get_input(self,  input_message: str, target: str):
        input_answer = input(f"\033[3{self.__target_color}m" + f"[{target}]: " + "\033[39m" + f"{input_message}\n: ").strip()
        if input_answer == "exit":
            self.exit_game()

        return input_answer
    
    def show_error(self, text):
        print(f'\033[3{self.__error_color}m' + text + '\033[39m' + "\n")

    def show_win(self, text):
        print(f'\033[3{self.__win_color}m' + text + '\033[39m' + "\n")

    def show_empate(self, text):
        print(f'\033[3{self.__empate_color}m' + text + '\033[39m' + "\n")
    
    def show_text(self, text):
        print(text + "\n")

    def exit_game(self):
        return super().exit_game()