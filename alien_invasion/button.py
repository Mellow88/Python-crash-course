"""Class Button"""

import pygame

class Button:
    """Class button Play"""
    def __init__(self, ai_game, msg, pos):
        """Ініціалізація атрибутів кнопки"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # NOTE: Задати розміри та властивості кнопки
        self.width, self.height = 200, 50
        self.x_pos, self.y_pos = pos[0], pos[1]
        self.button_color = (114, 128, 125)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # NOTE: Створити обєкт rect кнопки та відцентрувати його
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.top = self.y_pos

        # NOTE: Повідомлення на кнопцы треба показати лише один раз
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Перетворити текст на зображення та розмістити по центру кнопки"""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                                     self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def checkForInput(self, position):
        button_active = self.rect.collidepoint(position)
        if button_active:
            return True
        return False

    def draw_button(self):
        """Намалювати порожню кнопку а тоді -- повідомлення."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def update(self, msg):
        """Оновлення кнопок на екрані"""
        new_image = self.font.render(msg, True, self.text_color, None)
        self.screen.blit(new_image, self.msg_image_rect)

    def change_color(self, position):
        """Зміна кольору кнопки при наведенні на неї курсора мишки"""
        button_active = self.rect.collidepoint(position)
        if button_active:
            self.text_color = (0, 255, 85)
        else:
            self.text_color = (255, 255, 255)
