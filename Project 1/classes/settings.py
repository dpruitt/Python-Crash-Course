class Settings:

    def __init__(self):
        # screen
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (255, 255, 255)

        # bullets
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # aliens
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        # game stats
        self.ship_limit = 3