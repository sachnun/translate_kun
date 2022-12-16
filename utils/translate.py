from googletrans import Translator

tranlator = Translator()


class Translate:
    def __init__(self, text):
        self.text = text

    def translate(self):
        translated = tranlator.translate(self.text, dest="en")
        return translated.text

    def detect(self):
        detected = tranlator.detect(self.text)
        return detected.lang


if __name__ == "__main__":
    print(Translate("Hola").translate())
    print(Translate("Hola").detect())
