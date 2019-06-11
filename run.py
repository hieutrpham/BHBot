from vision import Vision
from control import Controller
from raid import Raid
from log import log
import argparse


vision = Vision()
controller = Controller()
raid = Raid(vision, controller)

def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=int, default=1, help='Number of raids')
    args = parser.parse_args()    

    for i in range(args.x):
        log(f'Start Raid {i+1}')
        raid.run()
        log(f'Raid {i+1} is done')

if __name__ == '__main__':
    run()
