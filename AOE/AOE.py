import threading
import time

from pynput import mouse,keyboard
mouse1=mouse.Controller()
keyboard1=keyboard.Controller()


def choose_first():
    mouse_pos0 = mouse1.position
    mouse1.position = (281, 641)
    time.sleep(0.07)
    mouse1.click(button=mouse.Button.left)

    mouse1.position = mouse_pos0
def on_click(x, y, button, pressed):
    if pressed:
        print(button)
    if str(button) == 'Button.x1' and pressed:
        choose_first()

def on_press(key):
    
    if str(key)=="Key.space":
        choose_first()

def on_release(key):
    pass

# time1=0
#
# def on_scroll(a,b,c,d):
#     global time1
#     if d==-1 and time.time()-time1>1:
#         choose_first()
#         time1=time.time()

def listen_mouse():
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

def listen_mouse_scroll():
    with mouse.Listener(on_scroll=on_scroll) as listener:
        listener.join()

def listen_keyboard():
    with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()



# t_m=threading.Thread(target=listen_mouse)
# t_m.start()

t_K=threading.Thread(target=listen_keyboard)
t_K.start()




# t_m.join()
t_K.join()
