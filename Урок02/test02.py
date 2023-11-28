import pygame as pg
from random import randint

import pygame.time


def main():
    size = width, height = 800, 600
    screen = pg.display.set_mode(size)
    flag = True
    fps = 120
    radius = 30
    clock = pg.time.Clock()
    running = True
    x = 0
    y = height // 2
    MYEVENT = pg.USEREVENT + 1
    pygame.time.set_timer(MYEVENT, 2000)
    while running:
        if flag:
            x, y = move(screen, x, y)
        draw(screen, x, y, radius)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                x, y = event.pos
                flag = False
            elif event.type == pg.MOUSEBUTTONUP:
                radius = 30
                flag = True
            elif event.type == pg.MOUSEMOTION and not flag:
                radius += 1
                x, y = event.pos
            elif event.type == MYEVENT:
                flag = True
                radius = 30
        pg.display.flip()
        screen.fill('black')
        clock.tick(fps)
    pg.quit()


def move(scr: pg.Surface, x, y):
    return (x + 1) % scr.get_width(), y


def draw(scr: pg.Surface, x, y, radius):
    pg.draw.circle(scr, 'red', (x, y), radius)


# for _ in range(1000):
#    x = randint(0, scr.get_width())
#    y = randint(0, scr.get_height())
#    scr.fill('white', (x, y, 1, 1))


if __name__ == '__main__':
    main()
