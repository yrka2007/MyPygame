import sys
import os
import pygame as pg
from const import *


def terminate():
    pg.quit()
    sys.exit()


def load_level(filename):
    fullname = os.path.join('levels', filename)
    with open(fullname, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


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


def start_screen(scr: pg.Surface):
    intro_text = ["ЗАСТАВКА", "",
                  "Правила игры",
                  "Если в правилах несколько строк,",
                  "приходится выводить их построчно"]

    fon = pg.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
    scr.blit(fon, (0, 0))
    font = pg.font.Font(None, 30)
    text_coord = 50
    clock = pg.time.Clock()
    for line in intro_text:
        string_rendered = font.render(line, 1, pg.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        scr.blit(string_rendered, intro_rect)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                terminate()
            elif event.type == pg.KEYDOWN or \
                    event.type == pg.MOUSEBUTTONDOWN:
                return
        pg.display.flip()
        clock.tick(FPS)


def finish_screen(scr: pg.Surface):
    fon = pg.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
    scr.blit(fon, (0, 0))
    font = pg.font.Font(None, 60)
    text_coord = 50
    clock = pg.time.Clock()
    string_rendered = font.render("ДО ВСТРЕЧИ!", 1, pg.Color('red'))
    intro_rect = string_rendered.get_rect()
    text_coord += 10
    intro_rect.top = text_coord
    intro_rect.x = 10
    text_coord += intro_rect.height
    scr.blit(string_rendered, intro_rect)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                terminate()
            elif event.type == pg.KEYDOWN or \
                    event.type == pg.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pg.display.flip()
        clock.tick(FPS)


class Tile(pg.sprite.Sprite):
    tile_images = {
        'wall': load_image('box.png'),
        'empty': load_image('grass.png')}

    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__()
        self.image = Tile.tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Player(pg.sprite.Sprite):
    player_image = load_image('mario.png')

    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = Player.player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)
