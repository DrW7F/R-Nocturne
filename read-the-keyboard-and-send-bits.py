import serial, time
from pynput.keyboard import Listener
import pygame

def key_recorder(key):
    key=str(key)
    if key == "'r'":
        dev = serial.Serial("COM3",115200)
        time.sleep(2)
        dev.write(b'1')
        dev.close()
        pygame.mixer.init()
        pygame.mixer.music.load('soung.mp3')
        pygame.mixer.music.play()
with Listener(on_press=key_recorder) as l:
    l.join()
