import cv2, pyautogui, os
from PIL import Image
import numpy as np
from mss import mss
from lib_hp.utilities import log

class Vision:

    def __init__(self):
        
        self.static_templates = {
            'cueCleared': os.getcwd() + r'\cues\cueCleared.png',
            'region_check': os.getcwd() + r'\cues\cueRegion.png',
            'cueAutoOff': os.getcwd() + r'\cues\cueAutoOff.png',
            'cueChat': os.getcwd() + r'\cues\cueChat.png',
            'cueFam': os.getcwd() + r'\cues\cueFam.png',
            'cueRIP': os.getcwd() + r'\cues\cueRIP.png'
           }

        self.templates = { k: cv2.imread(v, 0) for (k, v) in self.static_templates.items() }

        self.monitor = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}

        self.screen = mss()

        self.frame = None

    @staticmethod
    def getGameRegion():
        """Obtains the region of bit heroes. must be in guild hall to the top right of Quinn stable.
        Restart the browser if can't find game"""

        # identify the top-left Corner
        cueRegion = pyautogui.locateOnScreen(os.getcwd() + r'\cues\cueRegion.png')
        if cueRegion is None:
            raise Exception('Could not find game on screen. Is the game visible?')

        # calculate the region of the entire game
        topRightX = cueRegion[0] + cueRegion[2] # left + width
        topRightY = cueRegion[1] # top
        region = {'top': topRightX - 1000, 'left': topRightY, 'width': 1000, 'height': 651}
        return region

    def take_screenshot(self): 
        #take a screenshot of the game region and convert it to cv2 image
        sct_img = self.screen.grab(self.monitor)
        img = Image.frombytes('RGB', sct_img.size, sct_img.rgb)
        img = np.array(img)
        img = self.convert_rgb_to_bgr(img)
        self.frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return self.frame

    def get_image(self, path): #utility function to be used in unittesting
        return cv2.imread(path, 0)

    def bgr_to_rgb(self, img):
        b,g,r = cv2.split(img)
        return cv2.merge([r,g,b]) 

    def convert_rgb_to_bgr(self, img):
        return img[:, :, ::-1]

    def match_template(self, img_grayscale, template, threshold=0.9):
        """
        Matches template image in a target grayscaled image
        """
        res = cv2.matchTemplate(img_grayscale, template, cv2.TM_CCOEFF_NORMED)
        matches = np.where(res >= threshold)
        return matches

    def find_template(self, template, image=None, threshold=0.9):
        if image is None:
            if self.frame is None:
                self.take_screenshot()
            image = self.frame

        return self.match_template(
            image,
            self.templates[template],
            threshold
        )

# series of functions to help detect objects in game

    def found_cueCleared(self):
        matches = self.find_template('cueCleared')
        return np.shape(matches)[1] >= 1

    def found_cueChat(self):
        matches = self.find_template('cueChat')
        return np.shape(matches)[1] >= 1

    def found_cueFam(self):
        matches = self.find_template('cueFam')
        return np.shape(matches)[1] >= 1

    def found_cueAutoOff(self):
        matches = self.find_template('cueAutoOff')
        return np.shape(matches)[1] >= 1

    def found_cueRIP(self):
        matches = self.find_template('cueRIP')
        return np.shape(matches)[1] >= 1
