import os, sys
from typing import Union
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, RedirectResponse
from utils.translate import Translate
from pydictionary import Dictionary

# disable print
def blockPrint():
    sys.stdout = open(os.devnull, "w")


blockPrint()

tags_metadata = [
    {
        "name": "translate",
        "description": "Translate text to any language",
    },
    {
        "name": "detect",
        "description": "Detect language of text",
    },
    {
        "name": "dictionary",
        "description": "Get meaning, synonyms and antonyms of a word",
    },
]

description = """
A simple API to translate text to any language.\n
Its is free and open source.

[GitHub](https://github.com/sachnun/translate-kun)
"""

app = FastAPI(
    title="Translate-kun API",
    description=description,
    version="0.1.6",
    openapi_tags=tags_metadata,
    redoc_url=None,
    docs_url="/docs",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# redirect to docs
@app.get("/", include_in_schema=False)
def redirect():
    return RedirectResponse(url="/docs")


@app.get(
    "/languages",
    tags=["translate"],
    responses={
        200: {
            "description": "Successful Response",
            "content": {
                "application/json": {
                    "example": {
                        "message": "All languages available",
                        "lang": {
                            "af": "afrikaans",
                            "sq": "albanian",
                            "...": "...",
                        },
                    },
                },
            },
        },
    },
)
def languages():
    return JSONResponse(
        content={
            "message": "All languages available",
            "lang": Translate().languages(),
        },
        status_code=200,
    )


@app.get(
    "/translate",
    tags=["translate"],
    responses={
        200: {
            "description": "Successful Response",
            "content": {
                "application/json": {
                    "example": {
                        "text": "Hallo Dunia",
                        "translated": {
                            "text": "Hello World",
                            "pronunciation": "",
                            "lang": {
                                "detected": {
                                    "confidence": 1,
                                    "detected": "id",
                                    "meaning": "indonesian",
                                },
                                "dest": "en",
                            },
                        },
                    },
                },
            },
        },
        400: {
            "description": "Invalid destination language",
            "content": {
                "application/json": {
                    "example": {
                        "message": "Invalid destination language",
                        "lang": {
                            "af": "afrikaans",
                            "sq": "albanian",
                            "...": "...",
                        },
                    },
                },
            },
        },
    },
)
def translate(
    text: str,
    dest: Union[str, None] = "en",
    src: Union[str, None] = "auto",
    detect: bool = True,
):
    translate = Translate(text)

    # if invalid language
    if dest not in translate.languages():
        return JSONResponse(
            content={
                "message": "Invalid destination language",
                "lang": translate.languages(),
            },
            status_code=400,
        )

    return JSONResponse(
        content={
            "text": text,
            "translated": {
                "text": translate.translate(dest=dest, src=src),
                "pronunciation": translate.pronounce(),
                # if detect is true
                "lang": {
                    "detected": translate.detect() if detect else None,
                    "src": src,
                    "dest": dest,
                },
            },
        },
        status_code=200,
    )


@app.get(
    "/detect",
    tags=["detect"],
    responses={
        200: {
            "description": "Successful Response",
            "content": {
                "application/json": {
                    "example": {
                        "text": "Hallo Dunia",
                        "lang": {
                            "detected": {
                                "confidence": 1,
                                "detected": "id",
                                "meaning": "indonesian",
                            },
                            "src": "auto",
                            "dest": "en",
                        },
                    },
                },
            },
        },
    },
)
def detect(text: str):
    translate = Translate(text)
    return JSONResponse(
        content={
            "text": text,
            "lang": translate.detect(),
        },
        status_code=200,
    )


# dictionary
@app.get(
    "/dictionary",
    tags=["dictionary"],
    responses={
        200: {
            "description": "Successful Response",
            "content": {
                "application/json": {
                    "example": {
                        "text": "hello",
                        "dictionary": {
                            # "meanings": None,
                            "synonyms": ["greetings", "hi", "howdy"],
                            "antonyms": ["adios", "au revoir", "goodbye"],
                        },
                    },
                },
            },
        },
        422: {
            "description": "Invalid word",
            "content": {
                "application/json": {
                    "example": {
                        "message": "Invalid word, max 1 word",
                    },
                },
            },
        },
    },
)
# max 3 word
def dictionary(text: str = Query(..., regex="^[a-zA-Z ]{1,20}$"), meaning: bool = True):
    dictionary = Dictionary(text, 3)
    return JSONResponse(
        content={
            "text": text,
            "dictionary": {
                "meanings": dictionary.meanings() if meaning else None,
                "synonyms": dictionary.synonyms(),
                "antonyms": dictionary.antonyms(),
            },
        },
        status_code=200,
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
