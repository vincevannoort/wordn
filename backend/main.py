from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from game import Game
from validator import Validator

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return "This is the Wordn API"


@app.get("/start")
def start(length: int, category: Optional[str] = "standard"):
    return Game().start(length, category)


@app.post("/validate_word")
def validateWord(word: str, token: str):
    return Validator().validateWord(token, word)
