"""Alien invasion"""

# pylint: disable=e1101

import sys
import pygame
from time import sleep

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats

class AlienInvasion:
    """Загальний клас, що керує ресурсами та поведінкою гри."""

    def __init__(self):
        """Ініціалізація гри, створенння ресурсів гри"""
        pygame.init()
        pygame.display.set_caption("Alien Invasion")

        self.settings  = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        # NOTE: Створення екземпляру класу для збереження ігрової статистики
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def _update_screen(self):
        """Оновлення зображення на екрані"""
        # self.screen.fill(self.settings.bg_color)

        self.screen.blit(self.settings.background, (0, 0))

        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

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
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
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
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

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

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Реагування на зіткнення з кулями"""
        # NOTE: Перевірка чи котрась куля влучила в корабель прибульця
        # NOTE: Якщо куля влучила позбавляємось кулі і прибульця
        collisions = pygame.sprite.groupcollide(
            self.bullets,
            self.aliens,
            True,
            True)

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _create_fleet(self):
        """Створення флоту кораблів прибульців"""
        alien = Alien(self)
        alien_width, alien_height =  alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_alien_x = available_space_x // (2 * alien_width)

        # NOTE: Визначення кількості рядів прибульців,
        # NOTE: що поміщається на екрані
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                            (2 * alien_height) - ship_height)
        numbers_row = available_space_y // (3 * alien_height)

        for row_num in range(numbers_row):
            for alien_num in range(number_alien_x):
                self._create_alien(alien_num, row_num)

    def _create_alien(self, alien_num, row_num):
        """Створення корабля прибульця"""
        alien = Alien(self)
        alien_width, alien_height =  alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_num
        alien.y = alien.rect.height + 2 * alien.rect.height * row_num
        alien.rect.x = alien.x
        alien.rect.y = alien.y
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """
        Реагує відповідно до того, чи досяг котрийсь
        із прибульців краю екрана.
        """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Зміна напрямку руху флоту"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_aliens_bottom(self):
        """Перевірка чи прибулець не досяснуг нижньої частини екрану"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # NOTE: Зреагувати так ніби корабель було підбито
                self._ship_hit()
                break

    def _update_aliens(self):
        """"Оновлення позицій космічних кораблів прибульців"""
        self._check_fleet_edges()
        self.aliens.update()

        # NOTE: Перевірка зіткнення прибульців з кораблем
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            # print('Ship is hit!')
            self._ship_hit()

        # NOTE: Шукаємо прибульців що досягли краю екрану
        self._check_aliens_bottom()

    def _ship_hit(self):
        """Реагування на зіткнення прибульців з кораблем"""
        if self.stats.ships_left > 0:
            # NOTE: Зменшуємо кількість кораблів
            self.stats.ships_left -= 1

            # NOTE: Прибираємо залишок куль та прибульців
            self.aliens.empty()
            self.bullets.empty()

            # NOTE: Створення нового флоту та корабля
            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5)
        else:
            self.stats.game_active = False

    def run_game(self):
        """Початок головного циклу гри"""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()


if __name__ == '__main__':
    # NOTE: Створення екземпляру гри та її запуск
    ai = AlienInvasion()
    ai.run_game()
