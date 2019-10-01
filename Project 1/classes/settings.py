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

        # dynamic settings
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
