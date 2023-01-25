import random, io
from gtts import gTTS


class Speech:
    def __init__(self, language="en"):
        self.language = language

    def speak(self, text, save=False):
        tts = gTTS(text=text, lang=self.language)
        if save:
            filename = f"speech{random.randint(0, 100000)}.mp3"
            tts.save(filename)
            return filename
        else:
            f = io.BytesIO()
            tts.write_to_fp(f)
            f.seek(0)
            return f


if __name__ == "__main__":
    s = Speech()
    print(s.speak("Hello, world!", save=True))
