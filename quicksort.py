import pygame
import pygame.midi
import random
import datetime

FPS = 120
WIN_WIDTH = 900
WIN_HEIGHT = 600
WHITE = (255, 255, 255)

array = [i for i in range(127)] 
random.shuffle(array)
pygame.init()
pygame.midi.init()
pygame.font.init()

midi_port = pygame.midi.get_default_output_id()
print ("using output_id :%s:%s" % (midi_port, pygame.midi.get_device_info(midi_port)))
midi_out = pygame.midi.Output(midi_port, 1)
midi_out.set_instrument(25)

myfont = pygame.font.SysFont('Comic Sans MS', 30)

clock = pygame.time.Clock()
pygame.display.set_caption("quick sort")
screen = pygame.display.set_mode(
            (WIN_WIDTH, WIN_HEIGHT))

screen.fill(WHITE)

def QuickSort(array, l, r, screen, pygame, clock):
    if l >= r:
        return 
    else:
        q = random.choice(array[l:r + 1])
        i = l
        j = r
        while i <= j:
            while array[i] < q:
                i += 1
            while array[j] > q:
                j -= 1
            if i <= j: 
                DrawArray(pygame, screen, array, q, i, j)
                array[i], array[j] = array[j], array[i]
                i += 1
                j -= 1
                QuickSort(array, l, j, screen, pygame, clock)
                QuickSort(array, i, r, screen, pygame, clock)

def DrawArray(pygame, screen, array, q, i, j):
    x = 0
    y = (pygame.display.get_window_size()[1] // 3) * 2
    ORANGE = (255, 150, 100)
    GREEN = (67, 171, 134)
    RED = (255, 0, 0)
    BLUE = (0, 191, 255)
    screen.fill(WHITE)
    for element in array:
        rect = pygame.Rect(x, y, 6, -element * 2)
        rect.normalize()
        if element == array[q]:
            COLOR = RED
        elif element == array[i]:
            COLOR = GREEN
        elif element == array[j]:
            COLOR = BLUE        
        else:
            COLOR = ORANGE
        pygame.draw.rect(screen, COLOR, rect)
        x = x + 7
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    clock.tick(360)
    pygame.display.update()
    

QuickSort(array, 0, len(array) - 1, screen, pygame, clock)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()   
