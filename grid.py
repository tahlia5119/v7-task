import numpy as np
import copy
import random

class Grid:
    def __init__(self, size: int = 6):
        self.size = size
        # create the empty grid with a 2 tile randomly placed
        self.grid = np.zeros((size,size))
        self.grid[random.randint(0, size-1)][random.randint(0, size-1)] = 2

    def swipe_right(self):
        # loop through the rows
        for row_num, row in enumerate(self.grid):
            # remove values 0 (empty) or -1 (blocks - bonus task)
            temp_row = [v for v in row if v > 0]
            # add adjacent values starting from the right
            final_values = []
            i = len(temp_row)-1
            while i >= 0:
                if i != 0 and temp_row[i] == temp_row[i-1]:
                    final_values.append(temp_row[i]*2)
                    i = i - 2  # skip to next value since these were added together
                else:
                    final_values.append(temp_row[i])
                    i = i - 1

            # prepend zeros to get original length
            updated_row = [0] * (len(row) - len(final_values))
            updated_row.extend(reversed(final_values))  # using reversed as we are swiping right
            # update the grid object
            self.grid[row_num] = updated_row
        self.add_tile

    def swipe_left(self):
        # loop through the rows
        for row_num, row in enumerate(self.grid):
            # remove values 0 (empty) or -1 (blocks - bonus task)
            temp_row = [v for v in row if v > 0]
            # add adjacent values starting from the left
            final_values = []
            i = 0
            while i <= len(temp_row)-1:
                if i != len(temp_row)-1 and temp_row[i] == temp_row[i+1]:
                    final_values.append(temp_row[i]*2)
                    i = i + 2  # skip to next value since these were added together
                else:
                    final_values.append(temp_row[i])
                    i = i + 1

            # prepend zeros to get original length
            updated_row = [0] * (len(row) - len(final_values))
            final_values.extend(updated_row)
            # update the grid object
            self.grid[row_num] = final_values
        self.add_tile()

    def swipe_up(self):
        #TODO: is there a more efficient way than doing a deepcopy and two transposes?
        # create a copy of the grid and transpose it
        grid_t = copy.deepcopy(self.grid).transpose()
        # loop through the "rows"
        for row_num, row in enumerate(grid_t):
            # remove values 0 (empty) or -1 (blocks - bonus task)
            temp_row = [v for v in row if v > 0]
            # add adjacent values starting from the left
            final_values = []
            i = 0
            while i <= len(temp_row)-1:
                if i != len(temp_row)-1 and temp_row[i] == temp_row[i+1]:
                    final_values.append(temp_row[i]*2)
                    i = i + 2  # skip to next value since these were added together
                else:
                    final_values.append(temp_row[i])
                    i = i + 1

            # prepend zeros to get original length
            updated_row = [0] * (len(row) - len(final_values))
            final_values.extend(updated_row)
            # update the grid object
            grid_t[row_num] = final_values
        # transpose it back
        self.grid = grid_t.transpose()
        self.add_tile()

    def swipe_down(self):
        #TODO: is there a more efficient way than doing a deepcopy and two transposes?
        # create a copy of the grid and transpose it
        grid_t = copy.deepcopy(self.grid).transpose()
        # loop through the "rows"
        for row_num, row in enumerate(grid_t):
            # remove values 0 (empty) or -1 (blocks - bonus task)
            temp_row = [v for v in row if v > 0]
            # add adjacent values starting from the right
            final_values = []
            i = len(temp_row)-1
            while i >= 0:
                if i != 0 and temp_row[i] == temp_row[i-1]:
                    final_values.append(temp_row[i]*2)
                    i = i - 2  # skip to next value since these were added together
                else:
                    final_values.append(temp_row[i])
                    i = i - 1

            # prepend zeros to get original length
            updated_row = [0] * (len(row) - len(final_values))
            updated_row.extend(reversed(final_values)) # using reversed as we are swiping right
            # update the grid object
            grid_t[row_num] = updated_row
        # transpose it back
        self.grid = grid_t.transpose()
        # TODO: deduplicate this?
        self.add_tile()

    def add_tile(self):
        # check for number of empty tiles and get locations
        empty_tiles = []
        for row_num, row in enumerate(self.grid):
            for col_num, col in enumerate(row):
                if col == 0:
                    empty_tiles.append([row_num, col_num])
        # if there's only 1 space before we add the new tile then it's game over
        # TODO: raise custom error if this happens
        if len(empty_tiles) <= 1:
            print("GAME OVER")
            return
        
        # get a random index to choose which empty tile gets the new 2
        new_loc = empty_tiles[random.randint(0, len(empty_tiles)-1)]
        self.grid[new_loc[0]][new_loc[1]] = 2

        
