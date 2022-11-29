import pygame
########################################################################
from pygame.sprite import Sprite
########################################################################

class Ship(Sprite):
    """Class for the player's ship"""
    def __init__(self, ai_game):
        #Starting position
        super().__init__()
        self.screen = ai_game.screen
        self.screen_react = ai_game.screen.get_rect()
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_react.midbottom
        self.moving_right = False
        self.moving_left = False
        self.settings = ai_game.settings
        self.x = float(self.rect.x)
        self.moving_top = False
        self.moving_down = False
        self.y = float(self.rect.y)

    def update(self):
        """Location/speed of the ship, and screen lock"""
        if self.moving_right and self.rect.right < self.screen_react.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_react.bottom:
            self.y += self.settings.ship_speed
        if self.moving_top and self.rect.top > self.screen_react.top:
            self.y -= self.settings.ship_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Display ship"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_react.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    
