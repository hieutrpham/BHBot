import pyautogui, time
from vision import Vision
from log import log

class Controller:

    def leftClick(self, x, y):
        pyautogui.moveTo(x, y, 0.5)
        pyautogui.click()

    def click_cleared(self):
        log('Run is done')
        self.leftClick(448 + 335, 329 + 435)

    def click_persuade(self):
        log('Persuaded a Fam.')
        pyautogui.press('space')
        time.sleep(1)
        pyautogui.press('space')

    def click_xchat(self):
        log('Closing chat window.')
        self.leftClick(448 + 756, 329 + 136)

    def click_raid(self):
        self.leftClick(492, 735)
        log('Click Raid.')
        time.sleep(1.5)

    def click_summon(self):
        self.leftClick(448 + 679, 329 + 471)
        log('Click Summon Raid Boss.')
        time.sleep(1.5)

    def click_heroic(self):
        self.leftClick(448 + 738, 329 + 302)
        log('Choose Heroic Mode.')
        time.sleep(1.5)

    def click_accept(self):
        self.leftClick(448 + 649, 329 + 580)
        log('Accept and Go.')

    def click_auto(self):
        log('Resuming auto.')
        pyautogui.press('space')

    def click_potion(self):
        log('Click potion.')
        self.leftClick(448 + 54, 329 + 517)

    def click_revive(self):
        log('Using medium potion to revive.')
        self.leftClick(448 + 508, 329 + 318)
        time.sleep(.5)
        pyautogui.press('space')
