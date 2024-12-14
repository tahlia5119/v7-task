# V7 Take Home Task: 2048 Game

## Specifications

### Main Requirements
- The grid consists of 6x6 tiles
- At the beginning of a game the grid is empty, except for one tile of value 2 placed at random.
- The user can slide the tiles either up, down, left or right
- After each slide a new tile with value 1 will appear in a random free space.
- If there is no free space to put the new tile the game is lost
- During the slide, tiles of equal values pushed into each other will merge into a new tile with the combined value. 2 + 2 = 4
    - If there are 3 values next to each other, e.g. 2 2 2, and the player slides right, the values closest to the wall should merge first resulting in 2 4.
- If any tile reaches the value 2048 the game is won.


### Bonus Tasks
- Add randomly places obstacles into the grid :white_check_mark:
    -   the user should be able to choose the number of obstacles at the start of the game 
    - An obstacle acts as a wall and will not move
- Custom grid sizes :white_check_mark:
- A backend with support for multiplayer via websockets :negative_squared_cross_mark:

## Deploying and Playing

The app can be run (provided you have Docker) with the following command:

```bash
docker compose up frontend-app backend-app
```

This will build and deploy both backend and frontend containers. The game can then be acessed in the browser via http://localhost:8080.

You can use the `W`, `A`, `S` and `D` keys to select which direction to slide the tiles. There are also two inputs wherein you can select grid size and obstacle number.

## Solution

### Backend

I started off with the backend as that is where I am most familiar. I've chosen to use FastAPI library for a quick server deployment. I've focused on simply having an endpoint to which the frontend can make requests with the current state of the grid, game state, and the action the user wants to perform on the grid. If I were to develop this further to account for the multiplayer websocket bonus task, it should be quite easy to implement through FastAPI.

Regarding the functionality, I've kept it simple with using a small collection of functions that perform operations on the grid provided by the frontend depending on what key the user presses.

I was able to refine the main `push` functions but having the main logic in the `push_left` function and then using the following rules for the others:
- right - reverse the rows in the grid, call `push_left`, reverse back the rows in the grid
- up - transpose the grid, call `push_left`, transpose the grid back
- down - transpose the grid, call `push_right`, transpose the grid back

Other functions include adding a random `2` tile, adding obstacles, checking if any possible moves remain should there be no other space to add a tile, and creating a new grid based on the requested size. All of these can be found in `backend/grid.py`.

The base model used for the game endpoint has the following attributes:

| Attribute | Type  | Default| Description                               | Options                                   |
|-----------|-------|---------|------------------------------------------|-------------------------------------------|
| size      | int   | 6       | The length and width of the grid eg. 6x6 | `3 <= size <= 10`                         |
| blocks    | int   | 0       | Number of obstacles to add to the grid.  | `0 <= blocks <= size-2`                   |
| grid      | array | None    | `size`x`size` array of grid values       | N/A                                       |
| state     | str   | running | State of the game                        | `running`, `game_over`, `game_won`        |
| action    | str   |         | Action the player is taking              | `new_game`, `left`, `right`, `up`, `down` |

### Frontend

Given frontend is not my strong suit, I figured using Vue as V7 does would be more beneficial for me to learn. I've gone for VERY basic graphics to display the grid depending on the passed `size` and `blocks` parameters to the backend. Above the grid, there is a button `Reset Defaults` so that a user can quickly reset the `size` and `blocks` inputs to their defaults. The `Generate New Grid` button creates a new grid based on what's been input into `Number of Obstacles` and `Grid Size`.

To continue with the approach of simplicity, if an error occurs, the user inputs an invalid value, or the game is over, and alert appears to indicate so. For when the game is won, text indicates as such below the grid (see included images below). 

Obstacles are indicated by black squares.

I chose the colour pink because it's a nice colour and different from the original game :)

## Future Improvements

If time allowed, these are imrovements I would like to have made (and will possibly make once I've submitted this work):
- Bonus task: implement the websocket endpoint for multiplayer games
- UNIT TESTS
- Data persistence
    - I think it could be interesting to allow a user to return to an existing incomplete game
    - top scores
- a much more aesthetic frontend

Side note - everything in the `misc` folder is just what I created at the very start but thought could come in handy later. Nothing of interest there for the purpose of this take home coding task although I wrote notes throughout this process into NOTES.md which are messy but helped me track my thoughts and ideas.