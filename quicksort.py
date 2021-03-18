import pygame
import pygame.midi
import random
import datetime

FPS = 360
WIN_WIDTH = 1600
WIN_HEIGHT = 900
WHITE = (255, 255, 255)

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

def DrawArray(pygame, screen, array, q, i, j, l, r):
    
    """paygame -- python engyne
        scree - game screen
        array -- array to draw
        q -- pivot element
        i -- current index left pointer
        j -- current index right pointer 
        l -- left boarder subarray
        r -- right boarder subarry
    """
    t1 = datetime.datetime.now()
    
    WIN_WIDTH = pygame.display.get_window_size()[0]
    WIN_HEIGHT = pygame.display.get_window_size()[1]
    
    x = 0
    y = WIN_HEIGHT
    
    rectwidth =  (WIN_WIDTH - len(array)) // len(array)
    arraywidth = (rectwidth + 1) * len(array) 
    x = (WIN_WIDTH - arraywidth) // 2

    ORANGE = (255, 150, 100)
    GREEN = (67, 171, 134)
    RED = (255, 0, 0)
    BLUE = (0, 191, 255)
    BLACK = (0, 0, 0)
    FPS = 360
    screen.fill(WHITE)
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textInfo = myfont.render('pivot: %d l.index: %d r.index:%d' % (q, l, r), True, BLACK)
    
    for index in range(len(array)):   
        element = array[index]  
        rectheight = WIN_HEIGHT * element / max(array) 
        rect = pygame.Rect(x, y, rectwidth, -rectheight)
        rect.normalize()
        if element == q:
            COLOR = RED
        elif index == i:
            COLOR = GREEN
        elif index == j:
            COLOR = BLUE        
        else:
            COLOR = ORANGE   

        pygame.draw.rect(screen, COLOR, rect)
        
        if index == l:#element == array[l]:
            pygame.draw.line(screen, BLACK, (x, y), (x, -rectheight)) 

        if index == r:#element == array[r]:
            pygame.draw.line(screen, BLACK, (x + rectwidth, y), (x + rectwidth, -rectheight))

        x = x + (rectwidth + 1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    textFPSFrameTime = myfont.render('FPS: %d Frame cost: %f sec.' % (FPS, (datetime.datetime.now() - t1).microseconds / 1000000), True, BLACK)        
    screen.blit(textInfo, [10,10])
    screen.blit(textFPSFrameTime, [10,40])
    clock.tick(FPS)
    pygame.display.update()

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
                i = i + 1 if i + 1 < len(array)  else i  
                j = j - 1 if j - 1 >= 0 else j 
                DrawArray(pygame, screen, array, q, i, j, l, r)
        QuickSort(array, l, j, screen, pygame, clock)
        QuickSort(array, i, r, screen, pygame, clock)

running = True

while running:
    array = []
    for i in range(random.randint(10, 500)):
        array.append(random.randint(1, 20))
    random.shuffle(array)
    QuickSort(array, 0, len(array) - 1, screen, pygame, clock)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()   
