import re

from typing import Union
from fastapi import FastAPI

from util import roller

app = FastAPI()

@app.get("/")
def get_root():
    return { "status": "alive"}

@app.get("/dice/{roll}")
def get_dice_roll(roll: str):
    return roller.roll(roll)