#This code is written to find the co-ordinate of the mouse positiion on the screen.
#import pyautogui is used to import the pyautogui module which is used to automate some of the work.
import pyautogui

#def is syntax used to write function.
#Here a function named Info is created to get the position of the mouse on the screen in terms of x and y co-ordinates.
def Info():
    #data is a variable in which we store the position of the mouse co-ordinate.
    #pyautogui.position is in-built function that comes with the pyautogui module.
    data = pyautogui.position()
    print(data)


#from module time import sleep function
from time import sleep

#after running code there will be a 5 second pause so we get to arrange our mouse
sleep(5)
#run Info() function
Info()

