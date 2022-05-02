"""Class Alien"""

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Клас для керування космічним прибулцем."""

    def __init__(self, ai_game):
        """Ініціалізація прибульця та його початкового положення"""
        super().__init__()
        self.screen = ai_game.screen

        # NOTE: Завантаження зображення корабля
        image = pygame.image.load('images/alien_ship.bmp')
        # image = pygame.transform.scale(image, (64, 128))

        self.image = image
        self.rect = self.image.get_rect()

        # NOTE: Створення кожного нового корабля внизу по центру екрану
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # NOTE: Збереження десяткового значення позиції корабля по горизонталі
        self.x = float(self.rect.x)

    #     # NOTE: Індикатори руху
    #     self.moving_right = False
    #     self.moving_left = False
    #
    #     # self.moving_up = False
    #     # self.moving_down = False
    #
    # def update(self):
    #     """
    #     Оновлення поточної позиції корабля на основі
    #     індикатора руху
    #     """
    #     if self.moving_right and self.rect.right < self.screen_rect.right:
    #         self.x += self.settings.ship_speed
    #     if self.moving_left and self.rect.left > 0:
    #         self.x -= self.settings.ship_speed
    #
    #     self.rect.x = self.x
    #
    # def blitme(self):
    #     """Намалювати корабель у його поточному розташуванні"""
    #     self.screen.blit(self.image, self.rect)
