from googletrans import Translator
from googletrans import LANGUAGES

tranlator = Translator()


class Translate:
    def __init__(self, text=None):
        self.text = text
        self.pronunciation = None

    def translate(self, dest: str = "en"):
        translated = tranlator.translate(self.text, dest=dest)

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
                        "confidence": self.__percentage(confidence),
                        "detected": lang,
                        "meaning": self.__lang_meaning(lang),
                    }
                )
        else:
            data = {
                "confidence": self.__percentage(detected.confidence),
                "detected": detected.lang,
                "meaning": self.__lang_meaning(detected.lang),
            }

        return data

    def languages(self):
        return LANGUAGES

    def __lang_meaning(self, lang: str):
        return LANGUAGES.get(lang)

    def __percentage(self, value: float = 0.0):
        return str(round(value * 100, 2)) + "%"


if __name__ == "__main__":
    # print(Translate("Hola").translate())
    print(Translate("apa kabar").detect())
