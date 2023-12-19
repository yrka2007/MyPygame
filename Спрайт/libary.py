import pygame as pg
import sys
from random import randint
import os


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pg.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Bomb(pg.sprite.Sprite):
    image = load_image('bomb.png')
    image_boom = load_image('boom.png')

    def __init__(self, *args, x=0, y=0):
        super().__init__(*args)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, event: pg.event.Event) -> None:
        self.rect.x += randint(-4, 4)
        self.rect.y += randint(-4, 4)
        if event and event.type == pg.MOUSEBUTTONDOWN:
            if (self.rect.x < event.pos[0] < self.rect.x + self.rect.width) and (
                    self.rect.y < event.pos[1] < self.rect.y + self.rect.height):
                cx = self.rect.x + self.rect.width // 2
                cy = self.rect.y + self.rect.height // 2
                self.image = Bomb.image_boom
                self.rect = self.image.get_rect()
                self.rect.x = cx - self.rect.width // 2
                self.rect.y = cy - self.rect.height // 2


class Arrow(pg.sprite.Sprite):
    image = load_image('arrow.png')

    def __init__(self, *args, x=0, y=0):
        super().__init__(*args)
        self.image = Arrow.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, event: pg.event.Event) -> None:
        if event and event.type == pg.MOUSEMOTION:
            self.rect.x = event.pos[0]
            self.rect.y = event.pos[1]

class Hero(pg.sprite.Sprite):
    image = load_image('creature.png')

    def __init__(self, *args, x=0, y=0):
        super().__init__(*args)
        self.image = Hero.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, event: pg.event.Event) -> None:
        if event and event.type == pg.KEYDOWN:
            keys = pg.key.get_pressed()
            self.rect.x += 10 * (keys[pg.K_RIGHT] - keys[pg.K_LEFT])
            self.rect.y += 10 * (keys[pg.K_DOWN] - keys[pg.K_UP])
