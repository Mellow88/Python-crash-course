"""Alien invasion"""

# pylint: disable=e1101

import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """Загальний клас, що керує ресурсами та поведінкою гри."""

    def __init__(self):
        """Ініціалізація гри, створенння ресурсів гри"""
        pygame.init()
        pygame.display.set_caption("Alien Invasion")

        self.settings  = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))


        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def _update_screen(self):
        """Оновлення зображення на екрані"""
        self.screen.fill(self.settings.bg_color)
        # bg_img = pygame.image.load('images/background.jpg')
        # bg_img = pygame.transform.scale(bg_img,
        #          (self.settings.screen_width, self.settings.screen_height))
        #
        # self.screen.blit(bg_img, (0,0))
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()

    def _check_events(self):
        """Слідкування за подіями миші та клавіатури"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # NOTE: Перевіряємо чи натиснута клавіша
            # NOTE: Змінюємо атрибут moving_right корабля
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Реагування на натискання клавіш"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self, event):
        """Реагування, коли клавіша не натиснута"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Створити кулю та додати її до групи куль"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        # NOTE: Видалення куль, що зникли
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def run_game(self):
        """Початок головного циклу гри"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()


if __name__ == '__main__':
    # NOTE: Створення екземпляру гри та її запуск
    ai = AlienInvasion()
    ai.run_game()
