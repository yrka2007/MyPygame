import pygame as pg
from gameboard import Life


def main():
    size = width, height = 800, 600
    timer_time = 1000
    pg.init()
    clock = pg.time.Clock()
    fps = 50
    screen = pg.display.set_mode(size)
    objects = ()
    board = Life(16, 10)
    board.set_view(50, 20, 40)
    objects = objects + (board,)

    running = True
    live = False
    pg.time.set_timer(pg.USEREVENT, timer_time)
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN and not live:
                move_click(objects, event)
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    live = not live
            elif event.type == pg.USEREVENT and live:
                board.next_move()
            elif event.type == pg.MOUSEBUTTONDOWN and live:
                if event.button == 4:
                    timer_time = max(10, int(timer_time * 0.8))
                elif event.button == 5:
                    timer_time = min(1000, int(timer_time * 1.2))
                pg.time.set_timer(pg.USEREVENT, timer_time)

        if live:
            count = 0
            for el in board.board:
                count += sum(el)
            if count == 0:
                live = False
        else:
            pass

        screen.fill('blue')
        draw(objects, screen, live)
        pg.display.flip()
        clock.tick(fps)

    pg.quit()


def move_click(obj: tuple, event: pg.event):
    for item in obj:
        item.get_click(event)


def move_press(obj: tuple, event: pg.event):
    for item in obj:
        item.get_press(event)


def draw(obj: tuple, scr: pg.Surface, state):
    for item in obj:
        item.render(scr, state)


if __name__ == '__main__':
    main()
