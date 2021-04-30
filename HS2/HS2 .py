parameter1=1

import threading
import time

from pynput import mouse,keyboard
mouse1=mouse.Controller()

keyboard1=keyboard.Controller()




mouse_pos0=(0,0)
mouse_pos1=(0,0)


def on_click(x, y, button, pressed):
    pass


def on_press(key):
    print(key)

    global mouse_pos0
    global mouse_pos1

    if str(key)=="'e'":
        mouse_pos0 = mouse1.position
        mouse_pos1 = mouse1.position
    elif str(key)=="'q'":
        mouse1.position=mouse_pos0

    elif str(key) == "Key.alt_l":
        mouse1.position=mouse_pos1
        mouse1.press(mouse.Button.left)
    elif str(key) == "'s'":
        mouse1.release(mouse.Button.left)
        mouse_pos1 = mouse1.position

    elif str(key) == "'a'":
        mouse1.move(-parameter1, 0)
    elif str(key) == "'d'":
        mouse1.move(parameter1, 0)




def on_release(key):
    pass


def listen_mouse():
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

def listen_keyboard():
    with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()



t_m=threading.Thread(target=listen_mouse)
t_m.start()

t_k=threading.Thread(target=listen_keyboard)
t_k.start()


t_m.join()
t_k.join()
