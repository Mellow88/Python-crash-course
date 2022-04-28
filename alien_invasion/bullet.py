"""Bullet"""
#
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """docstring for Bullet."""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # NOTE: Створення rect кулі у (0. 0) та задати правильну позицію
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)

        self.rect.midtop = ai_game.ship.rect.midtop

        # NOTE: Збереження позиції корабля
        self.y = float(self.rect.y)

    def update(self):
        """Рух кулі"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Малюэмо кулю"""
        pygame.draw.rect(self.screen, self.color, self.rect)
