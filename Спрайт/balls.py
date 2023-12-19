import pygame as pg
from random import randint


class Ball(pg.sprite.Sprite):
    def __init__(self, radius, x, y):
        super().__init__(all_sprites)
        self.image = pg.Surface((2 * radius, 2 * radius),
                                pg.SRCALPHA, 32)
        pg.draw.circle(self.image, pg.Color("red"),
                       (radius, radius), radius)
        self.rect = self.image.get_rect()
        self.vx = randint(-5, 5)
        self.vy = randint(-5, 5)
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)
        if pg.sprite.spritecollideany(self, horizontal_borders):
            self.vy = -self.vy
        if pg.sprite.spritecollideany(self, vertical_borders):
            self.vx = -self.vx


class Border(pg.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:
            self.add(vertical_borders)
            self.image = pg.Surface([1, y2 - y1])
            self.rect = pg.Rect(x1, y1, 1, y2 - y1)
        else:
            self.add(horizontal_borders)
            self.image = pg.Surface([x2 - x1, 1])
            self.rect = pg.Rect(x1, y1, x2 - x1, 1)


horizontal_borders = pg.sprite.Group()
vertical_borders = pg.sprite.Group()
all_sprites = pg.sprite.Group()
size = WIDTH, HEIGHT = 500, 500
RADIUS = 20
pg.init()
screen = pg.display.set_mode(size)
FPS = 50
clock = pg.time.Clock()

Border(5, 5, WIDTH - 5, 5)
Border(5, HEIGHT, WIDTH - 5, HEIGHT - 5)
Border(5, 5, 5, HEIGHT - 5)
Border(WIDTH - 5, 5, WIDTH - 5, HEIGHT - 5)

for _ in range(20):
    Ball(20, WIDTH // 2 - RADIUS, HEIGHT // 2 - RADIUS)
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill('black')
    all_sprites.update()
    all_sprites.draw(screen)
    pg.display.flip()
    clock.tick(FPS)
pg.quit()
