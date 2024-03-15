import re

from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

from util.roller import Roll, RollResult

app = FastAPI()

@app.get("/")
def get_root():
    return { "status": "alive"}

@app.get("/dice/{roll}")
def get_dice_roll(roll: str) -> RollResult:
    
    return Roll(roll)