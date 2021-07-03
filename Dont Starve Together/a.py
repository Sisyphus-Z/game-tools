pickup_bar="'f'"
auto_run_bar="'z'"


import threading
import time
from pynput import mouse,keyboard

mouse1=mouse.Controller()
keyboard1=keyboard.Controller()

press_m=False
last_realse_mouse_by_keyf=False

def on_click(x, y, button, pressed):

    global press_m
    global last_realse_mouse_by_keyf
    # if str(button) == 'Button.left' and pressed==True:
    #     press_m=True
    if str(button) == 'Button.left' and pressed==False :

        # 通过按下f的松开左键不触发置press为False
        if last_realse_mouse_by_keyf == True:
            pass

        # 其他情况松开左键（比如用户按鼠标）触发：
        else:
            press_m=False






def on_press(key):

    global press_m
    global last_realse_mouse_by_keyf

    if str(key) == auto_run_bar:
        mouse1.press(button=mouse.Button.left)
        press_m=True
    if str(key) == pickup_bar:
        last_realse_mouse_by_keyf = True
        mouse1.release(button=mouse.Button.left)

    if str(key) in ("'w'","'a'","'s'","'d'"):
        mouse1.release(button=mouse.Button.left)




def on_release(key):

    global press_m
    global last_realse_mouse_by_keyf

    if str(key) == pickup_bar and press_m==True:

        mouse1.press(button=mouse.Button.left)

    last_realse_mouse_by_keyf = False




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
