from googletrans import Translator
from googletrans import LANGUAGES

tranlator = Translator()


class Translate:
    def __init__(self, text=None):
        self.text = text
        self.pronunciation = None

    def translate(self, dest: str = "en", src: str = "auto"):
        translated = tranlator.translate(self.text, dest=dest, src=src)

        if translated.pronunciation and translated.pronunciation != translated.text:
            self.pronunciation = translated.pronunciation

        return translated.text

    def pronounce(self):
        return self.pronunciation

    def detect(self):
        detected = tranlator.detect(self.text)

        data = []
        # check if detected list
        if isinstance(detected.lang, list):
            data = []
            for lang, confidence in zip(detected.lang, detected.confidence):
                data.append(
                    {
                        # "confidence": self.__percentage(confidence),
                        "confidence": confidence,
                        "detected": lang,
                        "meaning": self.__lang_meaning(lang),
                        "emoji": self.__emoji_flag(lang),
                    }
                )
        else:
            data = {
                # "confidence": self.__percentage(detected.confidence),
                "confidence": detected.confidence,
                "detected": detected.lang,
                "meaning": self.__lang_meaning(detected.lang),
                "emoji": self.__emoji_flag(detected.lang),
            }

        return data

    def languages(self):
        return LANGUAGES

    def __lang_meaning(self, lang: str):
        return LANGUAGES.get(lang)

    def __percentage(self, value: float = 0.0):
        return str(round(value * 100, 2)) + "%"

    def __emoji_flag(self, country_code: str = None):
        emoji = {
            "af": "🇦🇫",
            "sq": "🇦🇱",
            "am": "🇦🇲",
            "ar": "🇦🇪",
            "hy": "🇦🇲",
            "az": "🇦🇿",
            "eu": "🇪🇸",
            "be": "🇧🇾",
            "bn": "🇧🇩",
            "bs": "🇧🇦",
            "bg": "🇧🇬",
            "ca": "🇪🇸",
            "ceb": "🇵🇭",
            "ny": "🇿🇼",
            "zh-cn": "🇨🇳",
            "zh-tw": "🇹🇼",
            "co": "🇫🇷",
            "hr": "🇭🇷",
            "cs": "🇨🇿",
            "da": "🇩🇰",
            "nl": "🇳🇱",
            "en": "🇬🇧",
            "eo": "🇪🇸",
            "et": "🇪🇪",
            "tl": "🇵🇭",
            "fi": "🇫🇮",
            "fr": "🇫🇷",
            "fy": "🇳🇱",
            "gl": "🇪🇸",
            "ka": "🇬🇪",
            "de": "🇩🇪",
            "el": "🇬🇷",
            "gu": "🇮🇳",
            "ht": "🇭🇹",
            "ha": "🇳🇬",
            "haw": "🇺🇸",
            "iw": "🇮🇱",
            "he": "🇮🇱",
            "hi": "🇮🇳",
            "hmn": "🇨🇳",
            "hu": "🇭🇺",
            "is": "🇮🇸",
            "ig": "🇳🇬",
            "id": "🇮🇩",
            "ga": "🇮🇪",
            "it": "🇮🇹",
            "ja": "🇯🇵",
            "jw": "🇮🇩",
            "kn": "🇮🇳",
            "kk": "🇰🇿",
            "km": "🇰🇭",
            "ko": "🇰🇷",
            "ku": "🇮🇷",
            "ky": "🇰🇬",
            "lo": "🇱🇦",
            "la": "🇻🇦",
            "lv": "🇱🇻",
            "lt": "🇱🇹",
            "lb": "🇱🇺",
            "mk": "🇲🇰",
            "mg": "🇲🇬",
            "ms": "🇲🇾",
            "ml": "🇮🇳",
            "mt": "🇲🇹",
            "mi": "🇳🇿",
            "mr": "🇮🇳",
            "mn": "🇲🇳",
            "my": "🇲🇲",
            "ne": "🇳🇵",
            "no": "🇳🇴",
            "or": "🇮🇳",
            "ps": "🇦🇫",
            "fa": "🇮🇷",
            "pl": "🇵🇱",
            "pt": "🇵🇹",
            "pa": "🇮🇳",
            "ro": "🇷🇴",
            "ru": "🇷🇺",
            "sm": "🇼🇸",
            "gd": "🇬🇧",
            "sr": "🇷🇸",
            "st": "🇿🇦",
            "sn": "🇿🇼",
            "sd": "🇮🇳",
            "si": "🇱🇰",
            "sk": "🇸🇰",
            "sl": "🇸🇮",
            "so": "🇸🇴",
            "es": "🇪🇸",
            "su": "🇮🇩",
            "sw": "🇰🇪",
            "sv": "🇸🇪",
            "tg": "🇹🇯",
            "ta": "🇮🇳",
            "te": "🇮🇳",
            "th": "🇹🇭",
            "tr": "🇹🇷",
            "uk": "🇺🇦",
            "ur": "🇵🇰",
            "ug": "🇨🇳",
            "uz": "🇺🇿",
            "vi": "🇻🇳",
            "cy": "🇬🇧",
            "xh": "🇿🇦",
            "yi": "🇮🇱",
            "yo": "🇳🇬",
            "zu": "🇿🇦",
        }

        return emoji.get(country_code, "🇺🇳")


if __name__ == "__main__":
    # print(Translate("Hola").translate())
    print(Translate("apa kabar").detect())
