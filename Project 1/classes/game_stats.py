class GameStats:

    def __init__(self, game):
        self.settings = game.settings
        self.game_active = False
        self.file = open("data/high_score.txt", "r")
        self.high_score = int(self.file.read())
        self.file.close()
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def update_high_score(self, high_score):
        self.file = open("data/high_score.txt", "w")
        self.file.write(str(high_score))
        self.file.close()
