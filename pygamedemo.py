import pygame
import sys
import random
 
FPS = 120
WIN_WIDTH = 800
WIN_HEIGHT = 600
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)

array = [i for i in range(127)] 
random.shuffle(array)

clock = pygame.time.Clock()
sc = pygame.display.set_mode(
    (WIN_WIDTH, WIN_HEIGHT))
 
x = 0
# выравнивание по центру по вертикали
y = (WIN_HEIGHT // 3) * 2 
 
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
 
    # заливаем фон
    sc.fill(WHITE)
    
    for i in array:
        rect = pygame.Rect(x, y, 6, -i * 2)
        rect.normalize()
        pygame.draw.rect(sc, ORANGE, rect)
        x = x + 7                 
    # обновляем окно
    pygame.display.update()
    
    x = 0

    clock.tick(FPS)