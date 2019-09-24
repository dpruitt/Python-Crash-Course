class Settings:
    """A class to store all settings for Alien Invasion"""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (95, 184, 97)
        self.ship_speed = 5

        #Bullet Settings
        self.bullet_speed = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255,60,60)
        self.bullets_allowed = 5

        #Coin Settings
        self.coin_limit = 10
