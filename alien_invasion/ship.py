"""Class Ship"""

import pygame

class Ship():
    """Клас для керування космічним кораблем."""

    def __init__(self, ai_game):
        """Ініціалізація корабля та його початкового положення"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # NOTE: Завантаження зображення корабля
        image = pygame.image.load('images/space_ship.png')
        image = pygame.transform.scale(image, (64, 128))

        self.image = image
        self.rect = self.image.get_rect()


        # NOTE: Створення кожного нового корабля внизу по центру екрану
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Намалювати корабель у його поточному розташуванні"""
        self.screen.blit(self.image, self.rect)

print('test comment')
