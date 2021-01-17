import threading
import time

from pynput import mouse,keyboard
mouse1=mouse.Controller()
keyboard1=keyboard.Controller()

start_space=False

def space():
    while 1:
        while start_space==True:
            keyboard1.press(keyboard.Key.space)
            keyboard1.release(keyboard.Key.space)

            #keyboard1.press('a')
            #keyboard1.release('a')

            #keyboard1.press('d')
            #keyboard1.release('d')
            time.sleep(0.05)
        time.sleep(1)


def on_click(x, y, button, pressed):
    if str(button) == 'Button.right' :
        print('按住奔跑键')
        keyboard1.press('l')


def on_press(key):
    #print(key)
    global start_space
    if str(key)=="Key.shift":
        keyboard1.press('l')

    elif str(key)=="'g'":
        print('按住f')
        keyboard1.press('f')

    elif str(key)=="'c'":
        print('开始空格连点+左右键摇晃')
        start_space=True
    elif str(key)=="'v'":
        print('停止空格连点+左右键摇晃')
        start_space=False


def on_release(key):
    #print('弹起'+str(key))

    if str(key) == "Key.shift":
        keyboard1.release('l')



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

t_space=threading.Thread(target=space)
t_space.start()


t_space.join()
t_m.join()
t_k.join()
