import pygame as pg
import random

from const import *

pg.init()
screen = pg.display.set_mode(size)
clock = pg.time.Clock()
all_sprites = pg.sprite.Group()
pg.mixer.music.load('sounds/music.mp3')
pg.mixer.music.play(-1)
boom = pg.mixer.Sound('sounds/bum.ogg')
music_flag = True

from library import terminate, load_image, AnimatedSprite, Particle

def create_particles(position):
    # количество создаваемых частиц
    particle_count = 100
    # возможные скорости
    numbers = range(-5, 6)
    for _ in range(particle_count):
        Particle(position, random.choice(numbers), random.choice(numbers),
                 all_sprites)

# AnimatedSprite(load_image('red_man.png'), 7, 4, 100, 100, all_sprites)
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            terminate()
        elif event.type == pg.KEYDOWN:
            keys = pg.key.get_pressed()
            if keys[pg.K_SPACE]:
                if music_flag:
                    pg.mixer.music.pause()
                else:
                    pg.mixer.music.unpause()
                music_flag = not music_flag
        elif event.type == pg.MOUSEBUTTONDOWN:
            AnimatedSprite(load_image('red_man.png'), 7, 4, event.pos[0], event.pos[1], all_sprites)
            boom.play()
            create_particles(pg.mouse.get_pos())

    screen.fill('black')
    all_sprites.update()
    all_sprites.draw(screen)
    pg.display.flip()
    clock.tick(FPS)
