#Os module is used to perfom dependent functions of the operating system
import os
#import pyautogui is used to import the pyautogui module which is used to automate some of the work.
import pyautogui
#from module time import sleep function
from time import sleep
#Keyboard funtion is used for to automate typing amd other keyboard function
import keyboard

#Starts the Firefox application using the os module
os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Firefox")

#add a 4 second pause to get the firefox up and running
sleep (4)
#161 108
#this is co-ordinates of where my Whatsapp bookmark was in firefox. After starting firefox after 4 second mouse will move to written co-ordinate which we get from running the click.py program.
pyautogui.click(x=161, y=108)

#another 15 second sleep to give time to start whatsapp
sleep(15)
#Point(x=273, y=488)
#this is co-ordinate of the chat of the person you wanna text
pyautogui.click(x=257, y=317)

#another sleep for 5 seconds
sleep(5)
#co-ordinates of the place where we write our message(idk what its called text box ig) and press enter
pyautogui.click(x=888, y=1018)

sleep(2)
keyboard.write("This is an automated message")

sleep(2)
keyboard.press('enter')
