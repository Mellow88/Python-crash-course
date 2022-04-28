"""Class Ship"""

import pygame

class Ship():
    """Клас для керування космічним кораблем."""

    def __init__(self, ai_game):
        """Ініціалізація корабля та його початкового положення"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # NOTE: Завантаження зображення корабля
        image = pygame.image.load('images/space_ship.png')
        image = pygame.transform.scale(image, (64, 128))

        self.image = image
        self.rect = self.image.get_rect()


        # NOTE: Створення кожного нового корабля внизу по центру екрану
        self.rect.midbottom = self.screen_rect.midbottom

        # NOTE: Збереження десяткового значення позиції корабля по горизонталі
        self.x = float(self.rect.x)

        # NOTE: Індикатори руху
        self.moving_right = False
        self.moving_left = False

        # self.moving_up = False
        # self.moving_down = False

    def update(self):
        """
        Оновлення поточної позиції корабля на основі
        індикатора руху
        """

        
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        """Намалювати корабель у його поточному розташуванні"""
        self.screen.blit(self.image, self.rect)
