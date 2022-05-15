"""Alien invasion"""

# pylint: disable=e1101

import sys

from time import sleep

import random
import pygame


from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from explosion import Explosion
from button import Button
from scoreboard import ScoreBoard


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
        self.sb = ScoreBoard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.exlosions = pygame.sprite.Group()
        self._create_fleet()

        # NOTE: Створення кнопки "Play"
        self.play_button = Button(self, 'Play', (400, 400))
        self.quit_button = Button(self, 'Quit', (400, 470))

    def _update_screen(self):
        """Оновлення зображення на екрані"""
        self.screen.blit(self.settings.background, (0, 0))

        menu_font = self.settings.font
        menu_text = menu_font.render("Alien invasion", True, (255, 255, 255))
        menu_rect = menu_text.get_rect(center=(self.settings.screen_width/2, 150))
        mouse_pos = pygame.mouse.get_pos()

        # NOTE: Якщо гра неактивна малюємо кнопку 'Play'
        if not self.stats.game_active:
            self.screen.blit(menu_text, menu_rect)

            self.play_button.draw_button()
            self.play_button.change_color(mouse_pos)
            self.play_button.update('Play')

            self.quit_button.draw_button()
            self.quit_button.change_color(mouse_pos)
            self.quit_button.update('Quit')

        else:
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.ship.blitme()
            self.exlosions.draw(self.screen)
            self.aliens.draw(self.screen)
            self.sb.show_score()

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.play_button.checkForInput(mouse_pos):
                    self._check_play_button(mouse_pos)
                if self.quit_button.checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()
                    # self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
        """Реагування на натискання клавіш"""
        if event.key in (pygame.K_RIGHT, pygame.K_d):
            self.ship.moving_right = True
        elif event.key in (pygame.K_LEFT, pygame.K_a):
            self.ship.moving_left = True
        elif event.key in (pygame.K_UP, pygame.K_w):
            self.ship.moving_up = True
        elif event.key in (pygame.K_DOWN, pygame.K_s):
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self, event):
        """Реагування, коли клавіша не натиснута"""
        if event.key in (pygame.K_RIGHT, pygame.K_d):
            self.ship.moving_right = False
        elif event.key in (pygame.K_LEFT, pygame.K_a):
            self.ship.moving_left = False
        elif event.key in (pygame.K_UP, pygame.K_w):
            self.ship.moving_up = False
        elif event.key in (pygame.K_DOWN, pygame.K_s):
            self.ship.moving_down = False

    def _check_play_button(self, mouse_pos):
        """Реагування, коли клавіша не натиснута"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # NOTE: Анулювання ігрової статистики
            self.stats.reset_stats()
            self.stats.game_active = True
            self.settings.initialize_dynamic_settings()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            # NOTE: Видалення зайвих прибульців та куль
            self.aliens.empty()
            self.bullets.empty()

            # NOTE: Створення нового флоту
            self._create_fleet()
            self.ship.center_ship()

            # NOTE: Приховування курсора миші
            pygame.mouse.set_visible(False)

    def _fire_bullet(self):
        """Створити кулю та додати її до групи куль"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)

            new_bullet.color = (random.randint(0, 255),
                                random.randint(0, 255),
                                random.randint(0, 255))

            self.bullets.add(new_bullet)
            # SOM DO TIRO
            som = pygame.mixer.Sound('sounds/laser.wav')
            som.set_volume(0.3)
            som.play()

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

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self._alien_hit(collisions)
            self.sb.check_high_score()

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            self.stats.level += 1
            self.sb.prep_level()

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
            self.sb.prep_ships()

            # NOTE: Прибираємо залишок куль та прибульців
            self.aliens.empty()
            self.bullets.empty()

            # NOTE: Створення нового флоту та корабля
            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _alien_hit(self, hits):
        """Створення анімації вибуху космічних прибульців"""
        for hit in hits:
            expl = Explosion(hit.rect.center, 'lg')
            expl.rect.x = hit.rect.x
            expl.rect.y = hit.rect.y
            self.exlosions.add(expl)

    def run_game(self):
        """Початок головного циклу гри"""
        # Налаштування музики
        pygame.mixer.music.load('sounds/bg_music.mp3')
        pygame.mixer.music.set_volume(0.8)
        pygame.mixer.music.play(-1)
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                self.exlosions.update()

            self._update_screen()


if __name__ == '__main__':
    # NOTE: Створення екземпляру гри та її запуск
    ai = AlienInvasion()
    ai.run_game()
