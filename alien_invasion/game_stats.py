"""Class GameStats"""

import json

class GameStats():
    """Відстежування статистики гри"""

    def __init__(self, ai_game):
        """Ініціалізація статистики"""
        self.settings = ai_game.settings
        self.high_score = 0
        self.level = 1
        self.reset_stats()

        # NOTE: Початок гри в не активному стані
        self.game_active = False

    def reset_stats(self):
        """Скидування статистики"""
        self.ships_left = self.settings.ship_limit
        self.score = 0

    def load_stats_info(self, ref='saves/records.json'):
        """dddd"""
        try:
            with open(ref, encoding="utf8") as info:
                user_info = json.load(info)
                return user_info
        except FileNotFoundError:
            return 0

    def write_stats_info(self, user_name, user_record, ref='saves/records.json'):
        """Write game stats"""
        user_record = {user_name: user_record,}
        with open(ref, 'a', encoding="utf8") as game_stats:
            json.dump(user_record, game_stats)
            # sorted(game_stats.items(), key=lambda x: x[1])
