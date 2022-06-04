"""Class ScopeBoard"""

import pygame.font

from pygame.sprite import Group
from ship import Ship

import os

class ScoreBoard(object):
    """Class for update Scope."""

    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # NOTE: Налаштування шрифту
        self.text_color = (32, 240, 92)
        self.font = pygame.font.SysFont(None, 30)

        # NOTE: Підготовка зображення з початковим рахунком
        self.prep_score()
        self.prep_level()
        self.prep_ships()
        self.prep_high_score()

    def prep_score(self):
        """Перетворення рахунку на зображення"""
        rounded_score = round(self.stats.score, -1)
        score_str = "SCORE: " + "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                           None)

        # NOTE: Показ рахунку
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left + 20
        self.score_rect.top = 20

    def prep_level(self):
        """Перетворення рівня у зображення"""
        level_str = "Level: " + str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color,
                           None)

        # NOTE: Розташування рівня під рахунком
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.screen_rect.left + 20
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Show how many ships are left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left + 1):
            ship = Ship(self.ai_game)
            # image = pygame.image.load('images/space_ship.png')

            resource_path = os.path.dirname(__file__)
            image_path = os.path.join(resource_path, 'images')
            image = pygame.image.load(os.path.join(image_path, 'space_ship.png'))

            ship.image = pygame.transform.scale(image, (56, 37))
            ship.rect.x = self.ai_game.settings.screen_width -  ship_number * ship.rect.width/2
            ship.rect.y = 10
            self.ships.add(ship)



    def prep_high_score(self):
        """Перетворення рахунку на зображення"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "HIGH SCORE: " + "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                                self.text_color, None)

        # NOTE: Показати рекорд
        self.high_score_rect = self.score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 20#self.high_score_rect.top

    def show_score(self):
        """Показати рахунок на екрані."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def check_high_score(self):
        """Перевірка набраного рахунку"""
        # print(self.stats.load_stats_info())
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            if self.stats.ships_left == 0:
                self.stats.write_stats_info('user_1', self.stats.high_score)
            self.prep_high_score()
