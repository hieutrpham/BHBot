from vision import Vision
from control import Controller
import log
import numpy as np
import time, pyautogui

"""
All coordinates assume a screen resolution of 1920x1080, and Chrome
maximized with the Bookmarks Toolbar enabled.
game_size = {"width": 1000, "height": 651}
game must be in cinematic mode on kongregate website.
"""

class Raid:

    def __init__(self, vision, controller):
        self.vision = vision
        self.controller = controller

    def revive(self):
        """revive character using medium potion"""
        self.controller.click_potion()
        time.sleep(.5)

        matches = self.vision.find_template('cueRIP')
        time.sleep(.5)

        if np.shape(matches)[1] >= 1:

            x = matches[1][0] + 10
            y = matches[0][0] + 10

            self.controller.leftClick(x, y)
            time.sleep(.5)
            self.controller.click_revive()
            time.sleep(.5)
            self.controller.click_auto()

        else:
            pyautogui.press('escape')
            time.sleep(.5)
            self.controller.click_auto()


    def run(self):
    """game logic inluding autorevive and auto persuade fams using gold"""

        self.controller.click_raid()
        self.controller.click_summon()
        self.controller.click_heroic()
        self.controller.click_accept()

        while True:
            self.vision.take_screenshot()
            if self.vision.found_cueCleared():
                self.controller.click_cleared()
                break

            elif self.vision.found_cueAutoOff():
                self.revive()

            elif self.vision.found_cueFam():
                self.controller.click_persuade()

            elif self.vision.found_cueChat():
                self.controller.click_xchat()

            else:
                time.sleep(2)
