from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, RedirectResponse
from utils.translate import Translate

tags_metadata = [
    {
        "name": "translate",
        "description": "Translate text to any language",
    },
    {
        "name": "detect",
        "description": "Detect language of text",
    },
]

app = FastAPI(
    title="Translate-kun API",
    description="A simple API to translate text to any language",
    version="0.1.3",
    openapi_tags=tags_metadata,
    redoc_url="/redoc",
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


@app.get("/languages", tags=["translate"])
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
                            "lang": {
                                "detected": {
                                    "confidence": "100%",
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
    },
)
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
                            "confidence": "100%",
                            "detected": "id",
                            "meaning": "indonesian",
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
