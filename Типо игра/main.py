import pygame as pg
from const import *

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.key.set_repeat(200, 50)
from library import start_screen, finish_screen, terminate, load_level
from library import Tile, Player


def main(scr: pg.Surface):
    player = None

    all_sprites = pg.sprite.Group()
    tiles_group = pg.sprite.Group()
    player_group = pg.sprite.Group()
    curent_level = 0
    new_level = 1
    clock = pg.time.Clock()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                terminate()
            elif event.type == pg.KEYDOWN:
                keys = pg.key.get_pressed()
                if keys[pg.K_0]:
                    return
                elif keys[pg.K_1]:
                    new_level = 1
                elif keys[pg.K_2]:
                    new_level = 2
                elif keys[pg.K_3]:
                    new_level = 3
                old_xy = player.rect.x, player.rect.y
                player.rect.x += 10 * (keys[pg.K_RIGHT] - keys[pg.K_LEFT])
                player.rect.y += 10 * (keys[pg.K_DOWN] - keys[pg.K_UP])
                if pg.sprite.spritecollideany(player, tiles_group):
                    player.rect.x, player.rect.y = old_xy
        if curent_level != new_level:
            curent_level = new_level
            all_sprites = pg.sprite.Group()
            tiles_group = pg.sprite.Group()
            player_group = pg.sprite.Group()
            level = load_level(f'level{curent_level}.txt')
            player, sizex, sizey = generate_level(level, all_sprites, tiles_group, player_group)
        scr.fill('black')
        player_group.update()
        all_sprites.draw(scr)
        player_group.draw(scr)
        pg.display.flip()
        clock.tick(FPS)


def generate_level(level, asp, tsp, psp):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                t = Tile('empty', x, y)
                t.add(asp)
            elif level[y][x] == '#':
                t = Tile('wall', x, y)
                t.add(asp, tsp)
            elif level[y][x] == '@':
                t = Tile('empty', x, y)
                t.add(asp)
                new_player = Player(x, y)
                new_player.add(asp, psp)
    return new_player, x, y


if __name__ == '__main__':
    start_screen(screen)
    main(screen)
    finish_screen(screen)
