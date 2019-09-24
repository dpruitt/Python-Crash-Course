import sys
import pygame
import random

from settings import Settings
from ship import Ship
from bullet import Bullet
from coin import Coin

class AlienInvasion:
    """Overall Class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.settings = Settings()
        #self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.coins = []
        self.bullets = pygame.sprite.Group()
        self.score = 0



    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self.spawn_random_coin()
            # Watch for keyboard and mouse events
            self._check_events()
            # make the most recently drawn screen visible.
            self._update_screen()
            self.ship.update()
            for coin in self.coins:
                coin.update()
                if coin.rect.y > self.settings.screen_height + 50:
                    self.coins.remove(coin)
                if pygame.sprite.collide_rect(self.ship, coin):
                    self.coins.remove(coin)
                    self.score += 1
            self._update_bullets()
            pygame.display.flip()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right.
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move the ship to the left.
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        # get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for coin in self.coins:
            coin.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        largeText = pygame.font.Font('freesansbold.ttf', 40)
        TextSurf, TextRect = self.text_objects(f"Score: {self.score}", largeText)
        TextRect.x = self.settings.screen_width - 220
        TextRect.y = 15
        self.screen.blit(TextSurf, TextRect)
        pygame.display.flip()

    def spawn_random_coin(self):
        if len(self.coins) < self.settings.coin_limit:
            x = random.randrange(0, self.settings.screen_width)
            y = random.randrange(0, 200) * -1
            speed = random.randrange(1, 5)
            self.coins.append(Coin(self, x, y, speed))

    def text_objects(self, text, font):
        black = (0,0,0)
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()



if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()