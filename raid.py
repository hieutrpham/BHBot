from vision import Vision
from control import Controller
from log import log
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

        #coordinates of 5 members where RIP tombstones would be
        coordinates = [(829, 728), (764, 776), (636, 753), (565, 710), ( 697, 688)]

        for c in coordinates:
            # hover over each member's position to detect RIP
            pyautogui.moveTo(c[0],c[1],.5)
            img = self.vision.take_screenshot()
            matches = self.vision.match_template(img, self.vision.templates['cueRIP'])

            if np.shape(matches)[1] >= 1:
                log('Found a tombstone.')

                x = matches[1][0] + 10
                y = matches[0][0] + 10

                log('Click on tombstone')
                self.controller.leftClick(x, y)
                time.sleep(.5)
                self.controller.click_revive()
                log('Revive successful.')

            else:
                log("Couldn't find dead member at this position.")

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
                log('Someone dies. Attempt to revive.')
                self.revive()

            elif self.vision.found_cueFam():
                log('A familiar thinks you are cool. Attempt to persuade.')
                self.controller.click_persuade()

            elif self.vision.found_cueChat():
                self.controller.click_xchat()

            else:
                time.sleep(2)
