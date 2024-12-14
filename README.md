# V7 Take Home Task

This is a work in progress for a job application take home task. This readme will be significantly improved as I work on this task.

grid=6x6
use vue for frontend

## Process
started off with a `generate_grid` function that accepts a parameter of grid size (might as well take the bonus task into consideration now) and generates a matrix of 0 values and a 2 randomly places.

~~Add an `update_grid` function that accepts an integer corresponding to an action. At this point, I figured that the grid could be a class object that can update itself with these functions~~

Keeping the actions as their own standalone functions. For the up/down actions, I've used the numpy matrix `transpose` function on the original grid so needed to use `deepcopy` for this purpose. I'll probably want to look at optimising this as it doesn't seem like this is the most efficient method.

Next steps?
- add new random tile after an action - bring back `update_grid` function?
    - include check for a full grid
- abiltity to add obstacles (max 4) --> this will require refactoring this actions (they need to be deduplicated anyway
- add actual unit tests

Decided to use fastapi to expose the python backend to the frontend. I intend to set it up as a REST API wherein the grid state is sent to the backend with an action and a response is returned that includes game state (game over vs not game over) and the updated grid. If I have time, I can try the multiplayer bonus task with a websocket.

Given I'm using fastapi and the way the data is sent, I'm going to change from using a grid class to just basic functions. Might be useful for websockets though so I'll keep the file for now. I'll use the new `backend/grid.py` file to refine the functions.

Assuming minimum grid size is 4.

I'm including logic for the blocks now as that will be easier to implement as I go rather than later. I'm making an assumption that we can't have more than grid_size-2 blocks. Maybe I should change this to a solid 4 blocks? And that blocks cannot occur more than once in a row.

After some thinking, I really only need to define the push_left function and then the others can just use that combined wtih transpose/reverse operations.
left - left
right - reverse, left, reverse
up - transpose, left, transpose
down - transpose, right, transpose

Future improvements:
- data persistence 
    - allow user login so that they can return to their old game

