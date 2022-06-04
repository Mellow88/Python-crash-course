"""Сlass Explosion"""

import pygame
from pygame.sprite import Sprite

import os

class Explosion(Sprite):
    """fhdfdghdfg"""
    def __init__(self, center, size):
        Sprite.__init__(self)
        explosion_image = self._get_explosin_animation()
        self.size = size
        self.image = explosion_image[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 60

    def update(self):
        now = pygame.time.get_ticks()
        explosion_image = self._get_explosin_animation()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_image[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_image[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

    def _get_explosin_animation(self):
        """Отримуємо словник з картинками expolsion"""

        resource_path = os.path.dirname(__file__)
        image_path = os.path.join(resource_path, 'images')
        img_dir = os.path.join(image_path, 'explosions')

        # img_dir = 'images/explosions'
        explosion_anim = {}
        explosion_anim['lg'] = []
        explosion_anim['sm'] = []

        for i in range(9):
            file_name = f"ex_anim_0{i}.png"
            file_path = "/".join((img_dir, file_name))
            img = pygame.image.load(file_path).convert()
            img.set_colorkey((0, 0, 0))
            img_lg = pygame.transform.scale(img, (75, 75))
            explosion_anim['lg'].append(img_lg)
            img_sm = pygame.transform.scale(img, (32, 32))
            explosion_anim['sm'].append(img_sm)

            return explosion_anim
