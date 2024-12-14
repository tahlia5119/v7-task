from typing import Optional
from pydantic import BaseModel

import numpy as np
from fastapi import FastAPI


app = FastAPI()

class Game(BaseModel):
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
    return game