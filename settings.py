import pygame
########################################################################

class Settings:
    """Class for game settings"""
    def __init__(self):
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color =(170, 170, 170)
        self.ship_limit = 3
        self.bullet_width = 8
        self.bullet_height = 15
        self.bullet_color = (250, 250, 250)
        self.fleet_drop_speed = 10

        """Difficult change"""
        self.speedup_scale = 0.5
        self.score_scale = 1.5
        self.initialize_dynammic_settings()

    def initialize_dynammic_settings(self):
        """Difficult change"""
        self.ship_speed = 5
        self.bullet_speed = 5
        self.alien_speed = 5
        self.fleet_direction = 1
        self.bullet_allowed = 5
        self.alien_points = 10

    def increase_speed(self):
        """Difficult change"""
        self.ship_speed += self.speedup_scale
        self.bullet_speed += self.speedup_scale
        self.alien_speed += self.speedup_scale
        self.bullet_allowed += self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)


    
