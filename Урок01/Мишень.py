import pygame as pg


def main():
    N, K = [int(x) for x in input().split()]
    pg.init()
    width = height = (N * 2) * K
    size = width, height
    screen = pg.display.set_mode(size)
    draw(screen, width, height, K, N)
    pg.display.flip()
    while pg.event.wait().type != pg.QUIT:
        pass
    pg.quit()


def draw(scr: pg.surface.Surface, w, h, k, n):
    colors = [pg.Color('red'), pg.Color('green'), pg.Color('blue')]
    scr.fill((0, 0, 0))
    for i in range(k):
        id = k - i - 1
        wd = n * (k - i) * 2
        pg.draw.ellipse(scr, colors[id % 3], (i * n, i * n, wd, wd))


if __name__ == '__main__':
    main()
