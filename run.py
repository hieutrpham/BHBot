from vision import Vision
from control import Controller
from raid import Raid
from log import log

vision = Vision()
controller = Controller()
raid = Raid(vision, controller)


def run():
    num_raid = int(input('How many raids to run? '))
    for i in range(num_raid):
        log(f'Start Raid {i+1}')
        raid.run()
        log(f'Raid {i+1} is done')

if __name__ == '__main__':
    run()
