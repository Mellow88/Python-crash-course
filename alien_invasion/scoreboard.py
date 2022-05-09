"""Class ScopeBoard"""

import pygame.font

class ScoreBoard(object):
    """Class for update Scope."""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # NOTE: Налаштування шрифту
        self.text_color = (32, 240, 92)
        self.font = pygame.font.SysFont(None, 48)

        # NOTE: Підготовка зображення з початковим рахунком
        self.prep_score()


    def prep_score(self):
        """Перетворення рахунку на зображення"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                           None)

        # NOTE: Показ рахунку у рехньому правому куті
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_scope(self):
        """Показати рахунок на екрані."""
        self.screen.blit(self.score_image, self.score_rect)
