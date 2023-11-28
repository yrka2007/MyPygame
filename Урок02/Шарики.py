import pygame as pg

import pygame.time


def main():
    size = width, height = 800, 600
    screen = pg.display.set_mode(size)
    flag = True
    fps = 50
    clock = pg.time.Clock()
    running = True
    MYEVENT = pg.USEREVENT + 1
    pygame.time.set_timer(MYEVENT, 10)
    data = []
    while running:
        draw(screen, data)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN and event.button == pg.BUTTON_LEFT:
                x, y = event.pos
                data.append([x, y, -1, -1])
            elif event.type == MYEVENT:
                move(screen, data)
        pg.display.flip()
        screen.fill('black')
        clock.tick(fps)
    pg.quit()


def move(scr: pg.Surface, data: list):
    for i in range(len(data)):
        el = data[i]
        dx = el[2]
        dy = el[3]
        if not (0 + 10 <= el[0] <= scr.get_width() - 10):
            dx *= -1
        if not (0 + 10 <= el[1] <= scr.get_height() - 10):
            dy *= -1
        data[i] = el[0] + dx, el[1] + dy, dx, dy


def draw(scr: pg.Surface, data: list):
    for el in data:
        pg.draw.circle(scr, 'white', (el[0], el[1]), 10)


if __name__ == '__main__':
    main()
