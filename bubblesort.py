import pygame
import pygame.midi
import random
import datetime

FPS = 120
WIN_WIDTH = 900
WIN_HEIGHT = 600
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)
GREEN = (67, 171, 134)

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
pygame.display.set_caption("bubble sort")
screen = pygame.display.set_mode(
            (WIN_WIDTH, WIN_HEIGHT))
x = 0
y = (WIN_HEIGHT // 3) * 2

screen.fill(WHITE)

for i in range(len(array) - 1):
    for j in range(len(array) - 1 - i):
        t1 = datetime.datetime.now()
        note = array[j] 
        #midi_out.note_on(note,127)
        screen.fill(WHITE)
        for element in array:
                textIndexValue = myfont.render('index: %d value: %d' % (j, array[j]), True, (0, 0, 0))
                rect = pygame.Rect(x, y, 6, -element * 2)
                rect.normalize()
                COLOR = GREEN if element == array[j] else ORANGE
                pygame.draw.rect(screen, COLOR, rect)
                x = x + 7
        
        if array[j] > array[j + 1]:
            #midi_out.note_off(note, 127)
            array[j], array[j + 1] = array[j + 1], array[j]
            note = array[j] 
            #midi_out.note_on(note,127)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #midi_out.note_off(note, 127)
                pygame.quit()
        t2 = datetime.datetime.now()
        textFPSFrameTime = myfont.render('FPS: %d Frame coast: %f sec.' % (FPS, (t2 - t1).microseconds / 1000000), True, (0, 0, 0))
        #midi_out.note_off(note, 127)
        clock.tick(FPS)
        screen.blit(textIndexValue, [10,10])
        screen.blit(textFPSFrameTime, [10,40])
        pygame.display.update()
        x = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()   
