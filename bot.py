from PIL import ImageGrab
from PIL import ImageOps
import pyautogui
import time
from numpy import *

class Coordinates():
    replayBtn = (570,520)
    dino = (290,530)
    # x = 360 y = 560

def restartGame():
    pyautogui.click(Coordinates.replayBtn)

def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("Jump")
    pyautogui.keyUp('space')

#restartGame()
#time.sleep(1)
#pressSpace()

def imageGrab():
    box = (Coordinates.dino[0]+60 , Coordinates.dino[1],Coordinates.dino[0]+110 , Coordinates.dino[1]+35)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    s = a.sum()
    print(s)
    return s 
#while True:
 #   imageGrab()
def main():
    restartGame()
    while True:
        if(imageGrab()!=1997):
            pressSpace()
            time.sleep(0.1)
main()
