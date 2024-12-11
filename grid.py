import numpy as np

import random

class Grid:
    def __init__(self, size: int = 6):
        # create the empty grid with a 2 tile randomly placed
        self.grid = np.zeros((size,size))
        self.grid[random.randint(0, size-1)][random.randint(0, size-1)] = 2
    
    def update_grid(self, action: int):
        """Updates the grid dependent on the action

        :param actions: An int value representing an action - 0 = right, 1 = left, 2 = down, 3 = up
        :return: the updated grid
        """
        if action == 0:
            print("swiped right")
        elif action == 1:
            print("swiped left")
        elif action == 2:
            print("swiped down")
        elif action == 3:
            print("swiped up")
        else:
            print("action not recognised")
        
        # TODO: add self.grid = updated_grid
        
