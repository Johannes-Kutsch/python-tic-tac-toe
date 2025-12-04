from colorama import Style

from ColorManager import ColorManager


class PlayerManager:
    def __init__(self, player_1_name, player_2_name):
        self.active_player_id = 1
        self.player_1_name = player_1_name
        self.player_2_name = player_2_name
        pass

    def switch_active_player(self):
        if self.active_player_id == -1:
            self.active_player_id = 1
        else:
            self.active_player_id = -1

    def get_active_player_id(self):
        return self.active_player_id

    def get_active_player_name(self):
        return self.get_player_name(self.active_player_id)

    def get_active_player_color(self):
        return ColorManager.get_player_color(self.active_player_id)

    def get_player_name(self, player_id, color = True) -> str:
        return (ColorManager.get_player_color(player_id) if color else "") + (self.player_1_name if player_id == 1 else self.player_2_name) + (Style.RESET_ALL if color else "")
