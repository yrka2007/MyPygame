import pygame as pg


def main():
    size = width, height = [int(x) for x in input().split()]
    pg.init()
    screen = pg.display.set_mode(size)
    draw(screen, width, height)
    pg.display.flip()
    while pg.event.wait().type != pg.QUIT:
        pass
    pg.quit()


def draw(scr: pg.surface.Surface, w, h):
    scr.fill((0, 0, 0))
    color = pg.Color('white')
    pg.draw.line(scr, color, (0, 0), (w, h), 5)
    pg.draw.line(scr, color, (0, h), (w, 0), 5)


if __name__ == '__main__':
    main()
