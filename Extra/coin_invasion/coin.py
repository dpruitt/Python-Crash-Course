import pygame


class Coin:

    def __init__(self, ai_game, x, y, speed=1):
        """Initialize the coin and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images\coin.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        self.rect.y += self.speed

    def blitme(self):
        self.screen.blit(self.image, self.rect)