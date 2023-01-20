# Translate-kun API

A simple API to translate text to any language. It is free and open source.

## Features

*   Translate text to any language
*   Detect language of text
*   Dictionary of words

## Endpoints

### /languages

Get all languages available for translation.

#### Example Request

    GET /languages

#### Example Response

    {
        "message": "All languages available",
        "lang": {
            "af": "afrikaans",
            "sq": "albanian",
            "ar": "arabic",
            "...": "..."
        }
    }

### /translate

Translate text to any language.

#### Parameters

*   `text` (required): Text to be translated.
*   `dest` (optional): Destination language code. Default is `en`.
*   `src` (optional): Source language code. Default is `auto`.
*   `detect` (optional): Detect language of text. Default is `true`.

#### Example Request

    GET /translate?text=Hallo Dunia&dest=en

#### Example Response

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

## Usage

To use this API, you need to run the server.

    pip install -r requirements.txt
    uvicorn main:app --reload

## Support

If you have any questions or issues, please feel free to open an issue on [GitHub](https://github.com/sachnun/translate-kun).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/)