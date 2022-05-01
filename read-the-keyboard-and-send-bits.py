import serial, time
from pynput.keyboard import Listener


def key_recorder(key):
    key=str(key)
    if key == "'r'":
        dev = serial.Serial("COM3",115200)
        time.sleep(2)
        dev.write(b'1')
        dev.close()

with Listener(on_press=key_recorder) as l:
    l.join()
