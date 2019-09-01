import numpy as np
from PIL import ImageOps as io
import cv2
from matplotlib import pyplot as plt

# use this to test if cv2 could detect cues on a given screenshot

img = cv2.imread(r'test2.png', 0) # screenshot 
template = cv2.imread(r"..\cues\cueAutoOff.png", 0) # cue to match with the screenshot
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

print(np.shape(matches))
print(matches)
print(matches[1][0], matches[0][0])
print(min_val, max_val, min_loc, max_loc)

plt.show()

