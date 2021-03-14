import pygame
import sys
 
FPS = 30
WIN_WIDTH = 400
WIN_HEIGHT = 100
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)
 
clock = pygame.time.Clock()
sc = pygame.display.set_mode(
    (WIN_WIDTH, WIN_HEIGHT))
 
# радиус будущего круга
r = 30
# координаты круга
# скрываем за левой границей
x = 0 - r
# выравнивание по центру по вертикали
y = WIN_HEIGHT // 2
 
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
 
    # заливаем фон
    sc.fill(WHITE)
    # рисуем круг
    pygame.draw.circle(sc, ORANGE,
                       (x, y), r)
    # обновляем окно
    pygame.display.update()
 
    # Если круг полностью скрылся
    # за правой границей,
    if x >= WIN_WIDTH + r:
        # перемещаем его за левую
        x = 0 - r
    else:  # Если еще нет,
        # на следующей итерации цикла
        # круг отобразится немного правее
        x += 2
 
    clock.tick(FPS)