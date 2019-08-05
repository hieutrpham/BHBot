import pyautogui
import time
from log import log


# Coordinate constants that will be used in controller class 
RAID = (496, 701)
SUMMON = (1124, 761)
HEROIC = (1183, 592)
RAID_ACCEPT = (1097, 868)
AUTO_BUTTON = (1432, 654)


class Controller:

    def leftClick(self, x, y):
        pyautogui.moveTo(x, y, 0.5)
        pyautogui.click()

    def click_cleared(self):
        self.leftClick(448 + 335, 329 + 435)

    def click_persuade(self):
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
