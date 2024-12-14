from grid import Grid
import numpy as np
from backend.grid import push_left, push_right, push_up, push_down, new_grid

# grid = Grid()

# temp_grid = np.zeros((6,6))
# temp_grid[0][1] = 4
# temp_grid[0][5] = 4

# temp_grid[2][0] = 2
# temp_grid[2][1] = 4
# temp_grid[2][2] = 8
# temp_grid[2][3] = 16
# temp_grid[2][4] = 32
# temp_grid[2][5] = 64

# temp_grid[5][0] = 2
# temp_grid[5][2] = 2
# temp_grid[5][5] = 4

# print(temp_grid)
# grid.grid = temp_grid
# for i in range(261):
#     grid.swipe_down()
# print(grid.grid)

# # game over test
# full_grid = np.matrix([i for i in range(6)] for j in range(6))
# full_grid[0][0] = 0
# grid.grid = full_grid
# grid.swipe_down()

grid = np.array([[0, -1, 0, 2],[4, 4, 8, 0],[0, 0, -1, 2], [2, 0, 4, 4]])
print(push_down(grid))
print(new_grid(4, 2))