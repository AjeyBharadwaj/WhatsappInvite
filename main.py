import pywhatkit
import pyautogui
from tkinter import *
import datetime

win = Tk() # Some Tkinter stuff
screen_width = win.winfo_screenwidth() # Gets the resolution (width) of your monitor
screen_height= win.winfo_screenheight() # Gets the resolution (height) of your monitor

LOADING_TIME=20
CLOSING_WAIT_TIME=5

with open("phone_numbers.txt", "r") as fp:
    lines = fp.readlines()
    for line in lines:
        line = line.replace("\n", "")
        if "+91" not in line:
            line = "+91"+line
        ph_number = line
        print(f"Before {ph_number} : {datetime.datetime.now()}")
        contents = open("message.txt", encoding='utf8').read()
        pywhatkit.sendwhatmsg_instantly(ph_number, contents, tab_close=True, wait_time=LOADING_TIME, close_time=CLOSING_WAIT_TIME) 
        pyautogui.moveTo(screen_width * 0.694, screen_height* 0.964) # Moves the cursor the the message bar in Whatsapp
        pyautogui.click() # Clicks the bar
        pyautogui.press('enter') # Sends the message
        print(f"After {ph_number} : {datetime.datetime.now()}")
