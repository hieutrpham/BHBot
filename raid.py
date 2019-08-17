from log import log
import numpy as np
import time
import pyautogui

"""
All coordinates assume a screen resolution of 1920x1080, and Chrome
maximized with the Bookmarks Toolbar enabled.
game_size = {"width": 1000, "height": 651}
Game must be in cinematic mode on kongregate website.
"""


class Raid:

    def __init__(self, vision, controller):
        self.vision = vision
        self.controller = controller

    # deprecated
    def revive(self):
        """revive character using medium potion"""
        self.controller.click_potion()
        time.sleep(1)

        if self.vision.detect_uhoh():
            log('None of your units needs consumables.')
            pyautogui.press('space')
            time.sleep(.5)
            self.controller.click_auto()
        
        else:
            # coordinates of 5 members where RIP tombstones would be
            coordinates = {"first":(829, 728), "second":(764, 776), "third":(636, 753), "fourth":(565, 710), "fifth":(697, 688)}
            for k, v in coordinates.items():
                # hover over each member's position to detect RIP
                pyautogui.moveTo(v[0], v[1], .5)
                matches = self.vision.detect_cue('cueRIP')
                # if found tomestone, click on it
                if np.shape(matches)[1] >= 1:
                    log('Found a tombstone.')
                    for i in range(np.shape(matches)[1]):
                        x = matches[1][i] + 10 #2nd position of matches returns x coord
                        y = matches[0][i] + 10 #1st position of matches returns y coord
                        self.controller.leftClick(x, y)
                        log(f'Click on position {x, y}')
                        time.sleep(1)
                        if self.vision.detect_RevivePotion():
                            self.controller.click_revive()
                            log('Revive successful.')
                        else:
                            log('No average potion found.')
                            pyautogui.press('space')

                else:
                    log(f"Couldn't find dead member at the {k} position.")

            time.sleep(.5)
            self.controller.click_auto()

    def revive_revised(self):
        """revive character using medium potion"""
        self.controller.click_potion()
        time.sleep(1)

        if self.vision.detect_uhoh():
            log('None of your heroes needs pots.')
            pyautogui.press('space')
            time.sleep(.5)
            self.controller.click_auto()
        
        else:
            # coordinates of 5 members where RIP tombstones would be
            coordinates = {"1st":(829, 728), "2nd":(764, 776), "3rd":(697, 688), "4th":(636, 753), "5th":(565, 710)}
            for k, v in coordinates.items():
                try:
                    log(f'Attempt to revive the {k} hero')
                    self.controller.leftClick(v[0], v[1])
                    time.sleep(.5)
                    
                    if self.vision.detect_RevivePotion():
                        log(f'Hero at the {k} position is dead')
                        self.controller.click_revive()
                        log(f'Revive successful')
                        
                    elif self.vision.detect_HealthPotion(): #code here that detect health potion
                        log(f'Hero at the {k} position only needs heal')
                        pyautogui.press('escape')

                except Exception as e: log(f'Encounter some error: {e}')     
                
            self.controller.click_auto()     


    def run(self):
        """Main game loop"""

        self.controller.click_raid()
        self.controller.click_summon()
        self.controller.click_heroic()
        self.controller.click_accept()
        log('Go.')

        while True:
            self.vision.take_screenshot()
            if self.vision.found_cueCleared():
                self.controller.click_cleared()
                break

            elif self.vision.found_cueAutoOff():
                log('Someone dies. Attempt to revive.')
                self.revive_revised()

            elif self.vision.found_cueFam():
                log('A familiar thinks you are cool. Attempt to persuade.')
                self.controller.click_persuade()

            elif self.vision.found_cueChat():
                log('A chat window is opened. Do not disturbed when grinding!')
                self.controller.click_xchat()

            else:
                time.sleep(2)
