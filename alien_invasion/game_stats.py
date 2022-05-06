"""Class GameStats"""

class GameStats():
    """Відстежування статистики гри"""

    def __init__(self, ai_game):
        """Ініціалізація статистики"""
        self.settings = ai_game.settings
        self.reset_stats()

        # NOTE: Початок гри в не активному стані
        self.game_active = False

    def reset_stats(self):
        """Скидування статистики"""
        self.ships_left = self.settings.ship_limit
