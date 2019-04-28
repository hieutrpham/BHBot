import pyautogui as pg
import os, time
import numpy as np
from PIL import ImageOps as io
import cv2
from matplotlib import pyplot as plt

def screengrab():
    im = pg.screenshot()
    im.save(os.getcwd() + '\\checkRIP' + str(int(time.time())) +'.png', 'PNG')
    return im

def check_raid():
    box=(GAME_REGION[0]+325, GAME_REGION[1]+431, 165,45)
    im = io.grayscale(pg.screenshot(region=box))
    a = array(im.getcolors()).sum()
    print(a)
    return a
     
def get_cords():
    x,y = pg.position()
    x = x - x_pad
    y = y - y_pad
    print(x,y)

def detect(filename, region):
    if pg.locateOnScreen(filename, region = region) != None:
        print('Found Image')
    else:
        print('None')

#def vision():
img = cv2.imread('checkRIP1555854679.png', 0)
template = cv2.imread(r'C:\Users\hieup\Documents\GitHub\BHBot\cues\cueRIP.png', 0)
w, h = template.shape[::-1]
res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
matches = np.where(res >= 0.9)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
cv2.rectangle(img,top_left, bottom_right, 255, 5)
plt.subplot(121),plt.imshow(res,cmap = 'gray')
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img,cmap = 'gray')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
plt.show()
print(np.shape(matches))

def main():
    pass

if __name__ == '__main__':
    main()
