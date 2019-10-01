class GameStats:

    def __init__(self, game):
        self.settings = game.settings
        self.ships_left = self.settings.ship_limit
        self.game_active = False
        self.score = 0

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
