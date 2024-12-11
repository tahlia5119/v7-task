# V7 Take Home Task

This is a work in progress for a job application take home task. This readme will be significantly improved as I work on this task.

grid=6x6
use vue for frontend

## Process
started off with a `generate_grid` function that accepts a parameter of grid size (might as well take the bonus task into consideration now) and generates a matrix of 0 values and a 2 randomly places.

~~Add an `update_grid` function that accepts an integer corresponding to an action. At this point, I figured that the grid could be a class object that can update itself with these functions~~

Keeping the actions as their own standalone functions. For the up/down actions, I've used the numpy matrix `transpose` function on the original grid so needed to use `deepcopy` for this purpose. I'll probably want to look at optimising this as it doesn't seem like this is the most efficient method.