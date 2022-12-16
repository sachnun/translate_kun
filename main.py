from typing import Union
from fastapi import FastAPI
from utils.translate import Translate

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/translate")
def translate(text: str):
    return {"translated": Translate(text).translate()}
