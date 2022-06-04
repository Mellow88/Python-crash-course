"""Settings for game"""

import pygame
import os

class Settings():
    """Class for game settings."""

    def __init__(self):
        """Ініціалізація параметрів гри"""
        # Game settings
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        # self.bg_color = (230, 230, 230)

        bg_img = pygame.image.load(os.path.abspath('alien_invasion/images/background.png'))
        bg_img = pygame.transform.scale(bg_img, (self.screen_width,
                                                self.screen_height))
        self.background = bg_img
        
        # self.font = pygame.font.Font("fonts/main_font.ttf", 75)
        self.font = pygame.font.Font(os.path.abspath('alien_invasion/fonts/main_font.ttf'), 75)

        # Ship settings
        self.ship_limit = 5

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (159, 14, 22)
        self.bullets_allowed = 6

        # Alien settings
        self.fleet_drop_speed = 10

        # Explosion animation settings
        self.explosion_size = 'lg'

    def new_method(self, font):
        pygame.font.Font(font, 75)

    def initialize_dynamic_settings(self):
        """Ініціалізація змінних налаштувань"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.fleet_direction = 1   # напрямок руху 1 / -1

        # NOTE:
        self.alien_points = 50

    def increase_speed(self):
        """Збільшення налаштувань швидкості"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points)
