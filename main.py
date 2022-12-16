from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from utils.translate import Translate

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return JSONResponse(
        content={
            "message": "Welcome to the translation API",
            "description": "This API is used to translate text from one language to another",
            "version": "0.0.1",
            "endpoints": {
                "translate": {
                    "method": "GET",
                    "url": "/translate",
                    "params": {
                        "text": "The text to translate",
                        "dest": "The language to translate to (default: en)",
                    },
                }
            },
        },
        status_code=200,
    )


@app.get("/translate")
def translate(text: str, dest: Union[str, None] = "en"):
    translate = Translate(text)
    return JSONResponse(
        content={
            "text": text,
            "translated": {
                "text": translate.translate(dest=dest),
                "lang": {
                    "detected": translate.detect(),
                    "dest": dest,
                },
            },
        },
        status_code=200,
    )
