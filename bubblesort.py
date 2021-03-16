import pygame
import pygame.midi
import random

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
        
        note = array[j] 
        midi_out.note_on(note,127)
        screen.fill(WHITE)
        for element in array:
                text = myfont.render('index: %d value: %d' % (j, array[j]), True, (0, 0, 0))
                rect = pygame.Rect(x, y, 6, -element * 2)
                rect.normalize()
                COLOR = GREEN if element == array[j] else ORANGE
                pygame.draw.rect(screen, COLOR, rect)
                x = x + 7
        
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                midi_out.note_off(note, 127)
                pygame.quit()
        
        midi_out.note_off(note, 127)
        clock.tick(FPS)
        screen.blit(text, [10,10])
        pygame.display.update()
        x = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()   
