import pyautogui, time
from vision import Vision
from lib_hp.utilities import log

class Controller:
	
	def __init__(self):
		self.mouse = pyautogui

	def leftClick(self, x, y):
	    self.mouse.moveTo(x, y, 0.5)
	    self.mouse.click()

	def click_cleared(self):
	    log('Run is done')
	    self.leftClick(448 + 335, 329 + 435)

	def click_persuade(self):
		log('Persuaded a Fam.')
		self.mouse.press('space')
		time.sleep(1)
		self.mouse.press('space')
		
	def click_xchat(self):
	    self.leftClick(448 + 756, 329 + 136)

	def click_raid(self):
		self.leftClick(448 + 49, 329 + 407)
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
		self.mouse.press('space')

	def click_potion(self):
		self.leftClick(448 + 54, 329 + 517)

	def click_revive(self):
		self.leftClick(448 + 508, 329 + 318)
		time.sleep(.5)
		self.mouse.press('space')

