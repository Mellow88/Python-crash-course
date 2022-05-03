"""Class Alien"""

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Клас для керування космічним прибулцем."""

    def __init__(self, ai_game):
        """Ініціалізація прибульця та його початкового положення"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # NOTE: Завантаження зображення корабля
        image = pygame.image.load('images/alien_ship.png')
        image = pygame.transform.scale(image, (46, 42))

        self.image = image
        self.rect = self.image.get_rect()

        # NOTE: Створення кожного нового корабля внизу по центру екрану
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # NOTE: Збереження десяткового значення позиції корабля по горизонталі
        self.x = float(self.rect.x)

    def check_edges(self):
        """"Перевірка на досягнення краю екрана"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Зміщення космічного корабля прибульця"""
        self.x += (self.settings.alien_speed *
                  self.settings.fleet_direction)
        self.rect.x = self.x
