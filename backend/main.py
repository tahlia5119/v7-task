from typing import Optional
from pydantic import BaseModel

import numpy as np
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from backend.grid import new_grid, push_left, push_right, push_up, push_down, add_tile
from backend.custom_exceptions import GameOver, InvalidGameParameters


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Game(BaseModel):
    # parameters required to initialise new game otherwise can be none
    size: Optional[int] = 6
    blocks: Optional[int] = 0
    # matrix representing game grid
    grid: Optional[list] = None
    # string value of game state = running | game_over | game_won
    state: str = "running"
    # string value of action to perform = left | right | up | down | new_game
    action: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/game")
def play_game(game: Game):
    if game.grid is None or game.action == "new_game":
        try:
            game.grid = new_grid(game.size, game.blocks).tolist()
        except InvalidGameParameters as e:
            raise HTTPException(status_code=400, detail=str(e))

        game.state = "running"
    else:
        grid_np = np.array(game.grid)
        if game.action == "left":
            pushed = push_left(grid_np)
        elif game.action == "right":
            pushed = push_right(grid_np)
        elif game.action == "up":
            pushed = push_up(grid_np)
        elif game.action == "down":
            pushed = push_down(grid_np)
        else:
            game.state = "game_over" # TODO: or new_game?
            raise HTTPException(status_code=400, detail="Invalid action type.")

        # check if 2048 tile is present
        if len(np.where(pushed == 2048)) > 0:
            game.state = "game_won"

        try:
            game.grid = add_tile(pushed).tolist()
        except GameOver as e:
            raise HTTPException(status_code=200, detail=str(e))       
    
    return game