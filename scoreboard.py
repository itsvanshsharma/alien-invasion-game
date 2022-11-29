import pygame.font
################################################################
from pygame.sprite import Group
from ship import Ship
################################################################

class Scoreboard:
    """Class for scoring"""
    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.text_color = (250, 250, 250)
        self.font = pygame.font.SysFont('cursive', 50)
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
    
    def prep_score(self):
        """Generating score"""
        score_str = str(self.stats.score)
        rounded_score = round(self.stats.score, -1)
        score_str ="SCORE: " "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20       

    def prep_high_score(self):
        high_score = round(self.stats.high_score, -1)
        high_score_str = "HIGH SCORE: " "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 20
    
    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
    
    def prep_level(self):
        level_str = "LEVEL: " + str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 25
    
    def prep_ships(self):
        """Player life"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left +1):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width - 10
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)



