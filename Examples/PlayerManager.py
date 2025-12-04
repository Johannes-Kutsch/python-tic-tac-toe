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

    def get_player_name(self, player_id) -> str:
        return self.player_1_name if player_id == 1 else self.player_2_name