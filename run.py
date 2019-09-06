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
    parser.add_argument('num_raid', type=int, default=1, help='Number of raids', nargs='?')
    args = parser.parse_args()    
    
    log(f'Total raids to run: {args.num_raid}')

    defeat_num = 0

    for i in range(args.num_raid):
        log(f'Start Raid {i+1}')
        x = raid.run()
        if x == 1:
            defeat_num += 1
        log(f'Raid {i+1} is done')

    log(f'Success rate: {(args.num_raid - defeat_num)/args.num_raid * 100}%')
    log(f'Total defeat: {defeat_num} out of {args.num_raid} runs)

if __name__ == '__main__':
    run()
