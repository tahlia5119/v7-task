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
            updated_row.extend(final_values) # using reversed as we are swiping right
            # update the grid object
            grid_t[row_num] = updated_row
        # transpose it back
        self.grid = grid_t.transpose()


        
