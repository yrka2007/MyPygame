import pygame as pg


def main():
    pg.init()
    size = width, height = 800, 600
    screen = pg.display.set_mode(size)
    draw(screen)
    pg.display.flip()
    while pg.event.wait().type != pg.QUIT:
        pass
    pg.quit()


def draw(scr: pg.surface.Surface):
    scr.fill((0, 0, 0))



if __name__ == '__main__':
    main()
