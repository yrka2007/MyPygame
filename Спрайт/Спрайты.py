import pygame as pg
import sys
from random import randint
import os


def main():
    pg.init()
    size = width, height = 600, 400
    screen = pg.display.set_mode(size)
    from libary import Bomb
    clock = pg.time.Clock()
    fps = 50
    running = True

    all_sprites = pg.sprite.Group()
    for _ in range(50):
        Bomb(all_sprites, x=randint(0, width), y=randint(0, height))

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
