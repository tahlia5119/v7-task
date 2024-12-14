import numpy as np
import random

from backend.custom_exceptions import GameOver, InvalidGameParameters


def push_right(grid: np.ndarray) -> np.ndarray:
    # reverse order of values in each row
    rev_grid = np.flip(grid, 1)
    left = push_left(rev_grid)
    # reverse back
    return np.flip(left, 1)

def push_left(grid: np.ndarray) -> np.ndarray:
    updated_grid = np.ndarray((len(grid), len(grid)))
    for r, row in enumerate(grid):
        # if there are no blocks, we simply use just the row as one segment
        row_segments = [row]
        block = None
        
        # there should be max 1 block in each row (assumed)
        if -1 in row:
            block = list(row).index(-1)
            if block == len(row)-1:
                row_segments = [row[:-1]]
            elif block == 0:
                row_segments = [row[1:]]
            else:
                row_segments = [row[:block], row[block+1:]]
        # loop through each segment and push left
        updated_row = []
        for segment in row_segments:
            original_len = len(segment)
            non_zero = [v for v in segment if v > 0]
            # add adjacent values starting from the left
            updated_segment = []
            i = 0
            while i <= len(non_zero)-1:
                if i != len(non_zero)-1 and non_zero[i] == non_zero[i+1]:
                    updated_segment.append(non_zero[i]*2)
                    i = i + 2  # skip to next value since these were added together
                else:
                    updated_segment.append(non_zero[i])
                    i = i + 1
            # append zeros to get original length
            with_zeroes = [0] * (original_len - len(updated_segment))
            updated_segment.extend(with_zeroes)
            
            # add the final updated segment values to the row
            updated_row.extend(updated_segment)
        
        # add the block back into the row if it exists
        if block is not None:
            updated_row.insert(block, -1)
        
        updated_grid[r] = np.array(updated_row)
    
    return updated_grid
            
def push_down(grid: np.ndarray) -> np.ndarray:
    transposed = grid.transpose()
    right = push_right(transposed)
    down = right.transpose()
    return down

def push_up(grid: np.ndarray) -> np.ndarray:
    transposed = grid.transpose()
    left = push_left(transposed)
    up = left.transpose()
    return up

def add_tile(grid: np.ndarray) -> np.ndarray:
    # check for number of empty tiles and get locations
    empty_tiles = []
    for row_num, row in enumerate(grid):
        for col_num, col in enumerate(row):
            if col == 0:
                empty_tiles.append([row_num, col_num])
    # if there's only 1 space before we add the new tile then it's game over
    if len(empty_tiles) <= 1:
        raise GameOver("GAME OVER.")
    
    # get a random index to choose which empty tile gets the new 2
    new_loc = empty_tiles[random.randint(0, len(empty_tiles)-1)]
    grid[new_loc[0]][new_loc[1]] = 2

    return grid

def add_blocks(grid: np.ndarray, blocks: int = 0) -> np.ndarray:
    # each row and column can't have more than one block
    rows = list(range(0, len(grid)-1))
    cols = list(range(0, len(grid)))
    for _ in range(0, blocks):
        block_r = random.choice(rows)
        block_c = random.choice(cols)
        # remove chosen indices from choice
        rows.remove(block_r)
        cols.remove(block_c)
        # set grid with -1 for chosen location
        grid[block_r][block_c] = -1
    return grid

def new_grid(size: int = 6, blocks: int = 0) -> np.ndarray:
    # TODO: set these in a .env?
    if size < 3 or size > 10:
        raise InvalidGameParameters(f"Invalid grid size {size}. Must be between 3 and 10 (inclusive).")
    # create zeros matrix
    grid = np.zeros((size, size))
    # add blocks if required - maximum size-2 to avoid completely blocking sections of the grid
    if 0 <= blocks <= size-2:
        grid = add_blocks(grid, blocks)
    else:
        raise InvalidGameParameters(f"Invalid number of blocks {blocks} for grid size of {size}")
 
    # add random 2 tile and return
    return add_tile(grid)