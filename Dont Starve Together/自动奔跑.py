pickup_bar="'f'"
auto_run_bar="'z'"


import threading
import time
from pynput import mouse,keyboard

mouse1=mouse.Controller()
keyboard1=keyboard.Controller()

press_m=False
leftrelease_by_pickup=False
leftpress_by_autorunbar=False


release_by_right_key=False

press_m_by_mouse=False

press_pickup_bar=False
timer=0
def on_click(x, y, button, pressed):

    global press_m
    global leftrelease_by_pickup
    global leftpress_by_autorunbar
    global release_by_right_key
    global press_m_by_mouse

    if str(button) == 'Button.left' and pressed==True:
        press_m_by_mouse=True


    if str(button) == 'Button.left' and pressed==False:


        # 通过按下f的松开左键不触发置press_m为False
        if leftrelease_by_pickup == True:
            pass

        # 先按鼠标左键再按自动奔跑键时，松开鼠标左键后让鼠标左键也能继续按下
        elif leftpress_by_autorunbar==True:
            mouse1.press(button=mouse.Button.left)
            leftpress_by_autorunbar=False

        # 其他情况松开左键（比如用户按鼠标）触发：
        else:

            press_m=False


        leftpress_by_autorunbar = False
        press_m_by_mouse = False

    # elif str(button) == 'Button.right' and pressed==True and press_m==True:
    #     release_by_right_key=True
    #     mouse1.release(button=mouse.Button.left)
    #     print(33333333)
    #     release_by_right_key = False
    #
    # elif str(button) == 'Button.right' and pressed==False and press_m==True:
    #     release_by_right_key=True
    #     mouse1.press(button=mouse.Button.left)
    #     print(33333333)
    #     release_by_right_key = False



def on_press(key):

    global press_m
    global leftrelease_by_pickup
    global leftpress_by_autorunbar
    global press_pickup_bar
    global press_m_by_mouse

    if str(key) == auto_run_bar and press_m==False:
        if press_m_by_mouse==True:
            leftpress_by_autorunbar = True
        mouse1.press(button=mouse.Button.left)
        press_m=True





    elif str(key) == pickup_bar:
        leftrelease_by_pickup = True
        mouse1.release(button=mouse.Button.left)
        #press_pickup_bar = True

    # elif str(key) in ("'w'","'a'","'s'","'d'"):
    elif str(key) !=auto_run_bar:
        mouse1.release(button=mouse.Button.left)




def on_release(key):

    global press_m
    global leftrelease_by_pickup
    global press_pickup_bar
    global timer
    if str(key) == pickup_bar and press_m==True:
        mouse1.press(button=mouse.Button.left)

        timer=time.time()
        press_pickup_bar = False

    leftrelease_by_pickup = False




def listen_mouse():
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

def listen_keyboard():
    with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()

# def t_frequently_press_left_button():
#     global press_m
#     global press_pickup_bar
#     global timer
#
#     while True:
#         if press_m==True and press_pickup_bar==False and time.time()-timer<10:
#             mouse1.release(button=mouse.Button.left)
#             mouse1.press(button=mouse.Button.left)
#             press_m=True
#
#         time.sleep(0.4)



t_m=threading.Thread(target=listen_mouse)
t_m.start()

t_k=threading.Thread(target=listen_keyboard)
t_k.start()

# t_frequently_press_left_button=threading.Thread(target=t_frequently_press_left_button)
# t_frequently_press_left_button.start()

t_m.join()
t_k.join()
# t_frequently_press_left_button.join()
