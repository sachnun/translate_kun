import os, sys
from typing import Union
from fastapi import FastAPI, Query, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, RedirectResponse, StreamingResponse
from pydictionary import Dictionary

from utils.translate import Translate
from utils.dictionary import WordForm
from utils.spellchecker import Spellchecker
from utils.transcribe import Transcribe
from utils.speech import Speech


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
        "name": "dictionary",
        "description": "Dictionary is a tool that defines words",
    },
    {
        "name": "spellcheck",
        "description": "Spellchecker is a tool that checks the spelling of words",
    },
    {
        "name": "tts",
        "description": "Text to speech is a tool that converts text to speech",
    },
    {
        "name": "transcribe",
        "description": "Transcribe is a tool that converts speech to text",
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
    version="0.2.2",
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
    "/detect",
    tags=["translate"],
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
                            "meanings": [
                                "a greeting or salutation",
                                "an expression of greeting",
                            ],
                            "synonyms": ["greetings", "hi", "howdy"],
                            "antonyms": ["adios", "au revoir", "goodbye"],
                            "conjugate": {
                                "verb": ["hello", "helloed", "helloing", "hellos"],
                                "adjective": ["hello", "helloed", "helloing", "hellos"],
                                "noun": ["hello", "helloed", "helloing", "hellos"],
                                "adverb": ["hello", "helloed", "helloing", "hellos"],
                            },
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
    dictionary = Dictionary(text)
    conjugate = WordForm(text)
    return JSONResponse(
        content={
            "text": text,
            "dictionary": {
                "meanings": dictionary.meanings() if meaning else None,
                "synonyms": dictionary.synonyms(),
                "antonyms": dictionary.antonyms(),
                "conjugate": {
                    "verb": conjugate.get_verb(),
                    "adjective": conjugate.get_adjective(),
                    "noun": conjugate.get_noun(),
                    "adverb": conjugate.get_adverb(),
                },
            },
        },
        status_code=200,
    )


# spell check
@app.get(
    "/spellcheck",
    tags=["spellcheck"],
    responses={
        200: {
            "description": "Successful Response",
            "content": {
                "application/json": {
                    "example": {
                        "text": "helloo",
                        "spellcheck": ["helloo is not a word, did you mean hello?"],
                    },
                },
            },
        },
    },
)
def spellcheck(text: str, lang: str = "en-US"):
    spellcheck = Spellchecker(text, lang)
    return JSONResponse(
        content={
            "text": text,
            "spellcheck": spellcheck.messages(),
        },
        status_code=200,
    )


# text to speech
@app.get(
    "/tts",
    tags=["tts"],
    responses={
        200: {
            "description": "Successful Response",
            "content": {
                "audio/mp3": {
                    "example": {
                        "lang": "en",
                        "text": "hello",
                    },
                },
            },
        },
    },
)
def tts(
    # text with description
    text: str = Query(
        ...,
        description="Text to speech",
        example="hello",
    ),
    lang: str = "en",
):
    tts = Speech(lang)
    return StreamingResponse(
        content=tts.speak(text),
        media_type="audio/mp3",
        headers={
            "Content-Disposition": "attachment; filename=speech.mp3",
        },
    )


# post send audio file
@app.post(
    "/transcribe",
    tags=["transcribe"],
    responses={
        200: {
            "description": "Success",
            "content": {
                "application/json": {
                    "example": {
                        "message": "Success transcribe",
                        "data": {
                            "text": "saya ingin makan nasi goreng",
                            "confidence": 0.9,
                        },
                    }
                }
            },
        },
        400: {
            "description": "Bad Request",
            "content": {"application/json": {"example": {"detail": "File not found"}}},
        },
        500: {
            "description": "Internal Server Error",
            "content": {
                "application/json": {
                    "example": {"detail": "Internal Server Error"},
                }
            },
        },
    },
)
def transcribe(file: UploadFile = File(...)):
    # random filename
    import random
    import string

    filename = "".join(
        random.choice(string.ascii_uppercase + string.digits) for _ in range(10)
    )
    filename = f"{filename}.ogg"

    try:
        # save file
        with open(filename, "wb") as buffer:
            buffer.write(file.file.read())

        # transcribe
        transcribe = Transcribe()
        transcribe.load(filename)

        # return result
        return JSONResponse(
            status_code=200,
            content={
                "message": "Success transcribe",
                "data": {
                    "text": transcribe.text(),
                    "confidence": transcribe.confidence(),
                },
            },
        )
    except FileNotFoundError:
        return JSONResponse(
            status_code=400,
            content={"detail": "File not found"},
        )
    except Exception as e:
        print(e)
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal Server Error"},
        )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
