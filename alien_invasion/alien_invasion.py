"""Alien invasion"""

import sys
import pygame
from settings import Settings
from ship import Ship

class AlienIvasion:
    """Загальний клас, що керує ресурсами та поведінкою гри."""

    def __init__(self):
        """Ініціалізація гри, створенння ресурсів гри"""
        pygame.init()

        self.settings  = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def _update_screen(self):
        """Оновлення зображення на екрані"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

    def _check_events(self):
        """Слідкування за подіями миші та клавіатури"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def run_game(self):
        """Початок головного циклу гри"""
        while True:
            self._check_events()
            self._update_screen()


if __name__ == '__main__':
    # NOTE: Створення екземпляру гри та її запуск
    ai = AlienIvasion()
    ai.run_game()
