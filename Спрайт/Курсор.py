import pygame as pg


def main():
    pg.init()
    size = width, height = 800, 600
    screen = pg.display.set_mode(size)
    from libary import Arrow
    clock = pg.time.Clock()
    fps = 50
    running = True
    pg.mouse.set_visible(False)

    all_sprites = pg.sprite.Group()
    Arrow(all_sprites)
    while running:
        event = None
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            all_sprites.update(event)
        screen.fill('black')
        if pg.mouse.get_focused():
            all_sprites.draw(screen)
        pg.display.flip()
        clock.tick(fps)

    pg.quit()


if __name__ == '__main__':
    main()
