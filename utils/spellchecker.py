import language_tool_python
import json


class Spellchecker:
    def __init__(
        self,
        text=None,
        language="en-US",
    ):
        self.text = text
        self.language = language
        self.tool = language_tool_python.LanguageToolPublicAPI(self.language)

    def check(self):
        matches = self.tool.check(self.text)
        # list to json
        matches = [match.__dict__ for match in matches]
        return matches

    def messages(self):
        matches = self.check()
        messages = []
        for match in matches:
            messages.append(match["message"])
        return messages


if __name__ == "__main__":
    spellchecker = Spellchecker()
    text = "Our products experienced a drastic improvement ad a that time"
    print(spellchecker.messages(text))
