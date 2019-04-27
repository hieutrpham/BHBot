from vision import Vision
from control import Controller
from raid import Raid

vision = Vision()
controller = Controller()
raid = Raid(vision, controller)

def run():
	num_raid = int(input('How many raids to run? '))

	for i in range( num_raid):
		raid.run()

if __name__ == '__main__':
	run()

