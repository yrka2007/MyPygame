import pygame as pg
import sys
from random import randint
import os


def main():
    pg.init()
    size = width, height = 300, 300
    screen = pg.display.set_mode(size)
    from libary import Hero
    clock = pg.time.Clock()
    fps = 50
    running = True
    pg.key.set_repeat(200, 50)
    all_sprites = pg.sprite.Group()
    Hero(all_sprites)

    while running:
        event = None
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            all_sprites.update(event)
        screen.fill('white')
        all_sprites.draw(screen)
        pg.display.flip()
        clock.tick(fps)

    pg.quit()


if __name__ == '__main__':
    main()
