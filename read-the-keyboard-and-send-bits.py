import serial, pygame
from pynput.keyboard import Listener

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
dev.close()
