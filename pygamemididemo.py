import pygame
import pygame.midi
from time import sleep
import random
import os

def midiExample():
    # Things to consider when using pygame.midi:
    #
    # 1) Initialize the midi module with a to pygame.midi.init().
    # 2) Create a midi.Output instance for the desired output device port.
    # 3) Select instruments with set_instrument() method calls.
    # 4) Play notes with note_on() and note_off() method calls.
    # 5) Call pygame.midi.Quit() when finished. Though the midi module tries
    #    to ensure that midi is properly shut down, it is best to do it
    #    explicitly. A try/finally statement is the safest way to do this.
    #
    GRAND_PIANO = 0
    CHURCH_ORGAN = 19
    #instrument = CHURCH_ORGAN
    instrument = GRAND_PIANO
    
    pygame.init()
    pygame.midi.init()
    pygame.midi.get_device_info(0)
    port = 2 #pygame.midi.get_default_output_id()
    print ("using output_id :%s:" % port)
    midi_out = pygame.midi.Output(port, 1)
    try:
        midi_out.set_instrument(instrument)

        for i in range(0, 127):
            midi_out.note_on(i,127)
            midi_out.note_off(i,127)
            array = [i for i in range(127)]
            random.shuffle(array)
            print(array)
            os.system('clear')
            sleep(.2)



    finally:
        del midi_out
        pygame.midi.quit()

midiExample()