# Translate-kun API

Translate-kun API is a simple API that allows you to translate text to any language. It provides additional features such as language detection, dictionary definitions, spell checking, text-to-speech conversion, and speech-to-text transcription. This API is free and open source.

![screencapture-translate-kun-dakuport-eu-org-docs-2023-06-19-11_02_34](https://github.com/sachnun/translate-kun/assets/24667698/f9fcdc9a-04a7-4378-b544-2ea0d0b0a22d)

## Endpoints

### `/languages` - Get All Languages

- Method: GET
- Description: Retrieves a list of all available languages for translation.
- Response:
  - Status Code: 200 (OK)
  - Content-Type: application/json
  - Example Response Body:
    ```json
    {
      "message": "All languages available",
      "lang": {
        "af": "afrikaans",
        "sq": "albanian",
        "..." : "..."
      }
    }
    ```

### `/detect` - Language Detection

- Method: GET
- Description: Detects the language of the provided text.
- Query Parameters:
  - `text` (required): The text to detect the language from.
- Response:
  - Status Code: 200 (OK)
  - Content-Type: application/json
  - Example Response Body:
    ```json
    {
      "text": "Hallo Dunia",
      "lang": {
        "detected": {
          "confidence": 1,
          "detected": "id",
          "meaning": "indonesian"
        },
        "src": "auto",
        "dest": "en"
      }
    }
    ```

### `/translate` - Text Translation

- Method: GET
- Description: Translates the provided text to the specified language.
- Query Parameters:
  - `text` (required): The text to translate.
  - `dest` (optional): The destination language to translate the text to. Defaults to `"en"` (English).
  - `src` (optional): The source language of the text. Defaults to `"auto"` (automatic language detection).
  - `detect` (optional): Indicates whether to include language detection information in the response. Defaults to `true`.
- Response:
  - Status Code: 200 (OK)
  - Content-Type: application/json
  - Example Response Body:
    ```json
    {
      "text": "Hallo Dunia",
      "translated": {
        "text": "Hello World",
        "pronunciation": "",
        "lang": {
          "detected": {
            "confidence": 1,
            "detected": "id",
            "meaning": "indonesian"
          },
          "dest": "en"
        }
      }
    }
    ```
  - Status Code: 400 (Bad Request)
  - Content-Type: application/json
  - Example Response Body:
    ```json
    {
      "message": "Invalid destination language",
      "lang": {
        "af": "afrikaans",
        "sq": "albanian",
        "..." : "..."
      }
    }
    ```

### `/dictionary` - Word Dictionary

- Method: GET
- Description: Retrieves the meanings, synonyms, antonyms, and word forms (conjugations) of the provided word.
- Query Parameters:
  - `text` (required): The word to look up in the dictionary.
  - `meaning` (optional): Indicates whether to include meanings in the response. Defaults to `true`.
- Response:
  - Status Code: 200 (OK)
  - Content-Type: application/json
  - Example Response Body:
    ```json
    {
      "text": "hello",
      "dictionary": {
        "meanings": [
          "a greeting or salutation",
          "an expression of greeting"
       

 ],
        "synonyms": [
          "greetings",
          "hi",
          "howdy"
        ],
        "antonyms": [
          "adios",
          "au revoir",
          "goodbye"
        ],
        "conjugate": {
          "verb": [
            "hello",
            "helloed",
            "helloing",
            "hellos"
          ],
          "adjective": [
            "hello",
            "helloed",
            "helloing",
            "hellos"
          ],
          "noun": [
            "hello",
            "helloed",
            "helloing",
            "hellos"
          ],
          "adverb": [
            "hello",
            "helloed",
            "helloing",
            "hellos"
          ]
        }
      }
    }
    ```
  - Status Code: 422 (Unprocessable Entity)
  - Content-Type: application/json
  - Example Response Body:
    ```json
    {
      "message": "Invalid word, max 1 word"
    }
    ```

### `/spellcheck` - Spell Checking

- Method: GET
- Description: Checks the spelling of the provided text and suggests corrections if needed.
- Query Parameters:
  - `text` (required): The text to spell check.
  - `lang` (optional): The language to use for spell checking. Defaults to `"en-US"` (English).
- Response:
  - Status Code: 200 (OK)
  - Content-Type: application/json
  - Example Response Body:
    ```json
    {
      "text": "helloo",
      "spellcheck": [
        "helloo is not a word, did you mean hello?"
      ]
    }
    ```

### `/tts` - Text-to-Speech Conversion

- Method: GET
- Description: Converts the provided text into speech audio.
- Query Parameters:
  - `text` (required): The text to convert to speech.
  - `lang` (optional): The language of the text. Defaults to `"en"` (English).
- Response:
  - Status Code: 200 (OK)
  - Content-Type: audio/mp3
  - Example Response Body: Audio file in MP3 format.

### `/transcribe` - Speech-to-Text Transcription

- Method: POST
- Description: Transcribes the speech from the provided audio file.
- Request Body:
  - Form Data: Upload the audio file in the `file` field.
- Response:
  - Status Code: 200 (OK)
  - Content-Type: application/json
  - Example Response Body:
    ```json
    {
      "message": "Success transcribe",
      "data": {
        "text": "saya ingin makan nasi goreng",
        "confidence": 0.9
      }
    }
    ```
  - Status Code: 400 (Bad Request)
  - Content-Type: application/json
  - Example Response Body:
    ```json
    {
      "detail": "File not found"
    }
    ```
  - Status Code: 500 (Internal Server Error)
  - Content-Type: application/json
  - Example Response Body:
    ```json
    {
      "detail": "Internal Server Error"
    }
    ```

## Documentation and Usage

To view the API documentation and try out the endpoints, run the API server and access the documentation at `/docs` URL.

Example:
```
http://localhost:8000/docs
```

## Deployment

The API can be deployed using the `uvicorn` server. Run the following command to start the API server:

```shell
uvicorn main:app --host 0.0.0.

0 --port 8000
```

Make sure to replace `main` with the name of the Python file containing the code if it's different.

By default, the API server will run on `http://localhost:8000`. You can change the host and port according to your requirements.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please create an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - A modern, fast (high-performance), web framework for building APIs with Python 3.7+.
- [pydictionary](https://pypi.org/project/pydictionary/) - A Python library to get meanings, translations, synonyms, antonyms, and conjugations of words.
- Other dependencies used in the project are mentioned in the [requirements.txt](requirements.txt) file.
