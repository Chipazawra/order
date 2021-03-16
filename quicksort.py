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
        DrawArray(pygame, screen, array, q, i, j, l, r)
        while i <= j:
            while array[i] < q:
                i += 1
                DrawArray(pygame, screen, array, q, i, j, l, r)
            while array[j] > q:
                j -= 1
                DrawArray(pygame, screen, array, q, i, j, l, r)
            if i <= j:
                array[i], array[j] = array[j], array[i]
                DrawArray(pygame, screen, array, q, i, j, l, r)
                i += 1
                j -= 1
                DrawArray(pygame, screen, array, q, i, j, l, r)
        QuickSort(array, l, j, screen, pygame, clock)
        QuickSort(array, i, r, screen, pygame, clock)

def DrawArray(pygame, screen, array, q, i, j, l, r):
    t1 = datetime.datetime.now()
    x = 6
    y = (pygame.display.get_window_size()[1] // 3) * 2
    ORANGE = (255, 150, 100)
    GREEN = (67, 171, 134)
    RED = (255, 0, 0)
    BLUE = (0, 191, 255)
    BLACK = (0, 0, 0)
    FPS = 120
    screen.fill(WHITE)
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textInfo = myfont.render('pivot: %d l.index: %d r.index:%d' % (q, l, r), True, BLACK)
    
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
        
        if element == array[l]:
            pygame.draw.line(screen, BLACK, (x, y), (x, -element * 2)) 

        if element == array[r]:
            pygame.draw.line(screen, BLACK, (x + 6, y), (x + 6, -element * 2))

        x = x + 7
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    textFPSFrameTime = myfont.render('FPS: %d Frame coast: %f sec.' % (FPS, (datetime.datetime.now() - t1).microseconds / 1000000), True, BLACK)        
    screen.blit(textInfo, [10,10])
    screen.blit(textFPSFrameTime, [10,40])
    clock.tick(FPS)
    pygame.display.update()
    

QuickSort(array, 0, len(array) - 1, screen, pygame, clock)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()   
