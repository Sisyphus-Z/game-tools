import threading
import time

from pynput import mouse,keyboard
mouse1=mouse.Controller()
keyboard1=keyboard.Controller()

# def temp():
#     while 1:
#         keyboard1.press(keyboard.Key.space)
#         keyboard1.release(keyboard.Key.space)
#         time.sleep(2)
# t_temp=threading.Thread(target=temp)

def on_click(x, y, button, pressed):
    if str(button) == 'Button.right' and pressed==True:
        print('按下左shift')
        keyboard1.press(keyboard.Key.shift_l)


def on_press(key):
    if str(key)=="'g'":
        print('按下f')
        keyboard1.press('f')

    # if str(key)=="'b'":
    #     t_temp.start()
    #     t_temp.join

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

