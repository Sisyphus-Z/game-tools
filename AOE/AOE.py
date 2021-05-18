import threading
import time

from pynput import mouse,keyboard
mouse1=mouse.Controller()
keyboard1=keyboard.Controller()


def on_click(x, y, button, pressed):
    print(mouse1.position)

def on_press(key):
    if str(key)=="Key.f4":
        mouse_pos0=mouse1.position
        mouse1.position=(281, 641)
        mouse1.click(button=mouse.Button.left)
        mouse1.position=mouse_pos0

def on_release(key):
    pass

def listen_mouse():
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

def listen_keyboard():
    with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()



# t_m=threading.Thread(target=listen_mouse)
# t_m.start()

t_k=threading.Thread(target=listen_keyboard)
t_k.start()




# t_m.join()
t_k.join()
