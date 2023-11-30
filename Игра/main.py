import pygame as pg
from gameboard import Board


def main():
    size = width, height = 800, 600
    pg.init()
    clock = pg.time.Clock()
    fps = 50
    screen = pg.display.set_mode(size)
    objects = ()
    board = Board(16, 10)
    board.set_view(50, 20, 40)
    objects = objects + (board,)

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                move_click(objects, event)
            elif event.type == pg.KEYDOWN:
                move_click(objects, event)
        screen.fill('blue')
        draw(objects, screen)
        pg.display.flip()
        clock.tick(fps)

    pg.quit()


def move_click(obj: tuple, event: pg.event):
    for item in obj:
        item.get_click(event)


def move_press(obj: tuple, event: pg.event):
    for item in obj:
        item.get_press(event)


def draw(obj: tuple, scr: pg.Surface):
    for item in obj:
        item.render(scr)


if __name__ == '__main__':
    main()
