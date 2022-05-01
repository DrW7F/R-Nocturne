import serial, time
from pynput.keyboard import Listener
import pygame

dev = serial.Serial("COM3",115200)

def key_recorder(key):
    key=str(key)
    if key == "'r'":
        dev.write(b'1')
        pygame.mixer.init()
        pygame.mixer.music.load('song.mp3')
        pygame.mixer.music.play()
        

with Listener(on_press=key_recorder) as l:
    l.join()
    #time.sleep(10)
dev.close()
