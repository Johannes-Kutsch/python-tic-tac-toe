import os

class Utils:
    @staticmethod
    def clear_console():
        os.system('cls' if os.name == 'nt' else 'clear')