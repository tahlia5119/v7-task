from grid import Grid
import numpy as np

grid = Grid()

temp_grid = np.zeros((6,6))
temp_grid[0][1] = 4
temp_grid[0][5] = 4

temp_grid[2][0] = 2
temp_grid[2][1] = 4
temp_grid[2][2] = 8
temp_grid[2][3] = 16
temp_grid[2][4] = 32
temp_grid[2][5] = 64

temp_grid[5][0] = 2
temp_grid[5][2] = 2
temp_grid[5][5] =4

print(temp_grid)
grid.grid = temp_grid
grid.swipe_down()
print(grid.grid)
