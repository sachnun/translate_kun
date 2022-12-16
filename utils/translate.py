from googletrans import Translator

tranlator = Translator()


class Translate:
    def __init__(self, text):
        self.text = text

    def translate(self, dest: str = "en"):
        translated = tranlator.translate(self.text, dest=dest)
        return translated.text

    def detect(self):
        detected = tranlator.detect(self.text)

        data = []
        # check if detected list
        if isinstance(detected.lang, list):
            data = []
            for lang, confidence in zip(detected.lang, detected.confidence):
                data.append(
                    {
                        "confidence": self.__percentage(confidence),
                        "detected": lang,
                        "meaning": self.supported_languages(lang),
                    }
                )
        else:
            data = {
                "confidence": self.__percentage(detected.confidence),
                "detected": detected.lang,
                "meaning": self.supported_languages(detected.lang),
            }

        return data

    def supported_languages(self, lang: str = None):
        languages = {
            "af": "afrikaans",
            "sq": "albanian",
            "am": "amharic",
            "ar": "arabic",
            "hy": "armenian",
            "az": "azerbaijani",
            "eu": "basque",
            "be": "belarusian",
            "bn": "bengali",
            "bs": "bosnian",
            "bg": "bulgarian",
            "ca": "catalan",
            "ceb": "cebuano",
            "ny": "chichewa",
            "zh-cn": "chinese (simplified)",
            "zh-tw": "chinese (traditional)",
            "co": "corsican",
            "hr": "croatian",
            "cs": "czech",
            "da": "danish",
            "nl": "dutch",
            "en": "english",
            "eo": "esperanto",
            "et": "estonian",
            "tl": "filipino",
            "fi": "finnish",
            "fr": "french",
            "fy": "frisian",
            "gl": "galician",
            "ka": "georgian",
            "de": "german",
            "el": "greek",
            "gu": "gujarati",
            "ht": "haitian creole",
            "ha": "hausa",
            "haw": "hawaiian",
            "iw": "hebrew",
            "he": "hebrew",
            "hi": "hindi",
            "hmn": "hmong",
            "hu": "hungarian",
            "is": "icelandic",
            "ig": "igbo",
            "id": "indonesian",
            "ga": "irish",
            "it": "italian",
            "ja": "japanese",
            "jw": "javanese",
            "kn": "kannada",
            "kk": "kazakh",
            "km": "khmer",
            "ko": "korean",
            "ku": "kurdish (kurmanji)",
            "ky": "kyrgyz",
            "lo": "lao",
            "la": "latin",
            "lv": "latvian",
            "lt": "lithuanian",
            "lb": "luxembourgish",
            "mk": "macedonian",
            "mg": "malagasy",
            "ms": "malay",
            "ml": "malayalam",
            "mt": "maltese",
            "mi": "maori",
            "mr": "marathi",
            "mn": "mongolian",
            "my": "myanmar (burmese)",
            "ne": "nepali",
            "no": "norwegian",
            "or": "odia",
            "ps": "pashto",
            "fa": "persian",
            "pl": "polish",
            "pt": "portuguese",
            "pa": "punjabi",
            "ro": "romanian",
            "ru": "russian",
            "sm": "samoan",
            "gd": "scots gaelic",
            "sr": "serbian",
            "st": "sesotho",
            "sn": "shona",
            "sd": "sindhi",
            "si": "sinhala",
            "sk": "slovak",
            "sl": "slovenian",
            "so": "somali",
            "es": "spanish",
            "su": "sundanese",
            "sw": "swahili",
            "sv": "swedish",
            "tg": "tajik",
            "ta": "tamil",
            "te": "telugu",
            "th": "thai",
            "tr": "turkish",
            "uk": "ukrainian",
            "ur": "urdu",
            "ug": "uyghur",
            "uz": "uzbek",
            "vi": "vietnamese",
            "cy": "welsh",
            "xh": "xhosa",
            "yi": "yiddish",
            "yo": "yoruba",
            "zu": "zulu",
        }
        return languages[lang] if lang in languages else None

    def __percentage(self, value: float = 0.0):
        return str(round(value * 100, 2)) + "%"


if __name__ == "__main__":
    # print(Translate("Hola").translate())
    print(Translate("apa kabar").detect())
