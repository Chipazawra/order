import pygame
import sys
import random
 
FPS = 30
WIN_WIDTH = 640
WIN_HEIGHT = 480
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)

array = [i for i in range(127)] 
clock = pygame.time.Clock()
sc = pygame.display.set_mode(
    (WIN_WIDTH, WIN_HEIGHT))
 
x = 0
# выравнивание по центру по вертикали
y = WIN_HEIGHT // 2
 
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
 
    # заливаем фон
    sc.fill(WHITE)
    
    for i in array:
        pygame.draw.rect(sc, ORANGE, (x, y, 3, i))
        x = x + 6                 
    # обновляем окно
    pygame.display.update()
    
    x = 0
    random.shuffle(array)
    clock.tick(FPS)