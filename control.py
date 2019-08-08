import pyautogui
import time
from log import log

"""
Resolution must be set at 1920 x 1080, scale set at 125% on windows machines
"""

# Sometimes the y coordinate will be shifted from the original position. This delta is to adjust for that situation
DELTA = 40

# Coordinate constants that will be used in controller class
RAID = (496, 701+DELTA)
SUMMON = (1124, 761+DELTA)
HEROIC = (1183, 592+DELTA)
RAID_ACCEPT = (1097, 868+DELTA)
AUTO_BUTTON = (1432, 654+DELTA)


class Controller:

    def leftClick(self, x, y):
        pyautogui.moveTo(x, y, 0.5)
        pyautogui.click()

    def click_cleared(self):
        self.leftClick(448 + 335, 329 + 435)

    def click_persuade(self):
        self.leftClick(954,644)
        pyautogui.press('space')
        time.sleep(.5)
        pyautogui.press('space')

    def click_xchat(self):
        self.leftClick(448 + 756, 329 + 136)

    def click_raid(self):
        self.leftClick(RAID[0], RAID[1])
        time.sleep(1.5)

    def click_summon(self):
        self.leftClick(SUMMON[0], SUMMON[1])
        time.sleep(1.5)

    def click_heroic(self):
        self.leftClick(HEROIC[0], HEROIC[1])
        time.sleep(1.5)

    def click_accept(self):
        self.leftClick(RAID_ACCEPT[0], RAID_ACCEPT[1])

    def click_auto(self):
        log('Auto on.')
        self.leftClick(AUTO_BUTTON[0], AUTO_BUTTON[1])

    def click_potion(self):
        self.leftClick(448 + 54, 329 + 517)

    def click_revive(self):
        log('Using minor revive potion.')
        self.leftClick(730, 660)
        time.sleep(.5)
        pyautogui.press('space')
