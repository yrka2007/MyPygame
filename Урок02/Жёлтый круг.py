import pygame as pg

import pygame.time


def main():
    size = width, height = 800, 600
    screen = pg.display.set_mode(size)
    flag = True
    fps = 50
    radius = 1
    x, y = (-1, -1)
    clock = pg.time.Clock()
    running = True
    MYEVENT = pg.USEREVENT + 1
    pygame.time.set_timer(MYEVENT, 20)
    while running:
        move(screen)
        draw(screen, x, y, radius)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                x, y = event.pos
                flag = False
                radius = 1
            elif event.type == MYEVENT:
                radius += 1
        pg.display.flip()
        screen.fill('blue')
        clock.tick(fps)
    pg.quit()


def move(scr: pg.Surface):
    pass


def draw(scr: pg.Surface, x, y, radius):
    if x >= 0:
        pg.draw.circle(scr, 'yellow', (x, y), radius)


if __name__ == '__main__':
    main()
