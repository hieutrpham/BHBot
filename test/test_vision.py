import os, pyautogui
from mss import mss

def g():
    x, y = pyautogui.position()
    print(x, y)

coordinates = [(829, 728), (764, 776), (636, 753), (565, 710), (697, 688)]

for c in coordinates:
# hover over each member's position to detect RIP
    pyautogui.moveTo(c[0],c[1],.5)
