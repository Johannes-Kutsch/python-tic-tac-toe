class ColorManager:
    @staticmethod
    def get_player_color(player_id) -> str:
        return f"\033[38;5;75m" if player_id == 1 else f"\033[38;5;208m"

    @staticmethod
    def get_error_color() -> str:
        return f"\033[38;5;196m"