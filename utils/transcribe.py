import speech_recognition as sr
import subprocess
from os import path, remove


class Transcribe:
    # empty constructor
    def __init__(self):
        self.result = None
        pass

    def load(self, file):
        AUDIO_FILE = file

        # check if file exist
        if not path.exists(AUDIO_FILE):
            raise FileNotFoundError(f"File {AUDIO_FILE} not found")

        # convert ogg to wav
        filename = self.__convert(AUDIO_FILE)

        # use the audio file as the audio source
        r = sr.Recognizer()
        with sr.AudioFile(filename) as source:
            audio = r.record(source)
            # delete wav
            remove(filename)

        self.result = r.recognize_google(
            audio, language="id", show_all=True, with_confidence=True
        )

    def text(self):
        return self.result["alternative"][0]["transcript"].lower()

    def confidence(self):
        return self.result["alternative"][0]["confidence"]

    def __convert(self, file):
        # random filename
        import random
        import string

        filename = "".join(
            random.choice(string.ascii_uppercase + string.digits) for _ in range(10)
        )
        filename = f"{filename}.wav"

        # convert ogg to wav quiet
        subprocess.call(
            [
                "ffmpeg",
                "-i",
                file,
                filename,
                "-hide_banner",
                "-loglevel",
                "error",
                "-y",
            ]
        )
        # delete ogg
        remove(file)

        return filename


if __name__ == "__main__":
    transcribe = Transcribe()
    transcribe.load("audio_2023-01-18_01-58-18.ogg")

    print(transcribe.text())
    print(transcribe.confidence())
