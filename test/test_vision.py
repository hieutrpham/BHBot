import os, pyautogui
from mss import mss

def g():
    x, y = pyautogui.position()
    x = x - 261 #top
    y = y - 270 #left
    print(x, y)
    
def space():
    pyautogui.press('space')
    print('pressed')

cords = [(381+261, 400+270), (318+261, 437+270), (184+261, 422+270), (116+261, 382+270), (247+261, 363+270)]
for cord in cords:
    pyautogui.moveTo(cord[0], cord[1], .5)

