import pygame

n = int(input())
width1 = (150 // n) * 2
height1 = 300
x = 150 - 150 // n
y = 0
if __name__ == '__main__':
    pygame.init()
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    for i in range(n):
        pygame.draw.ellipse(screen, (255, 255, 255), (x, y, width1, height1), 1)
        pygame.draw.ellipse(screen, (255, 255, 255), (y, x, height1, width1), 1)
        width1 += (150 // n) * 2
        x -= 150 // n
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()