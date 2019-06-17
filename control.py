import pyautogui
import time
from log import log


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
        self.leftClick(492, 735)
        time.sleep(1.5)

    def click_summon(self):
        self.leftClick(448 + 679, 329 + 471)
        time.sleep(1.5)

    def click_heroic(self):
        self.leftClick(448 + 738, 329 + 302)
        time.sleep(1.5)

    def click_accept(self):
        self.leftClick(448 + 649, 329 + 580)

    def click_auto(self):
        log('Auto on.')
        self.leftClick(1432, 654)

    def click_potion(self):
        self.leftClick(448 + 54, 329 + 517)

    def click_revive(self):
        log('Using minor revive potion.')
        self.leftClick(730, 660)
        time.sleep(.5)
        pyautogui.press('space')
