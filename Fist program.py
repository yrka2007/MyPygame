import pygame


def main():
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    draw(screen)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()


def draw(scr: pygame.surface.Surface):
    scr.fill((0, 0, 0))
    pygame.draw.rect(scr, pygame.Color('Orange'), (10, 10, 500, 200))
    pygame.draw.circle(scr, (10, 0, 100), (300, 300), 200, 200)
    pygame.draw.line(scr, (0, 0, 255), (0, 0), (scr.get_width(), scr.get_height()), 10)
    pygame.draw.polygon(scr, (100, 0, 100), ((10, 10), (100, 500), (700, 200)))
    font = pygame.font.Font(None, 50)
    text = font.render("Hello, Pygame!", True, (100, 255, 100))
    text_x = scr.get_width() // 2 - text.get_width() // 2
    text_y = scr.get_height() // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    scr.blit(text, (text_x, text_y))
    pygame.draw.rect(scr, (0, 255, 0), (text_x - 10, text_y - 10,
                                           text_w + 20, text_h + 20), 1)


if __name__ == '__main__':
    main()
