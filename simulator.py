from pprint import pprint
from environment import *
import argparse

# set the random seeds for reproducibility
import random
import numpy as np
myseed=175175175
random.seed(myseed)
np.random.seed(myseed)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='ITSC 2024 Reproducibility in Transportation Research Tutorial')
    parser.add_argument('--run-idm', action='store_true')
    parser.add_argument('--run-custom', action='store_true')
    parser.add_argument('--no-render', action='store_true', default=False)
    args = parser.parse_args()

    pprint(vars(args))
    print("[INFO] Starting the simulator...")

    game = Environment(args)
    print("[INFO] Created Environment Object...")
    game.run()
    print("[INFO] End of the simulation...")
