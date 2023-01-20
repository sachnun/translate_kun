import json
from pydictionary import Dictionary
from word_forms.word_forms import get_word_forms


class DictionaryChecker:
    # empty constructor
    def __init__(self, limit=3):
        self.limit = limit
        pass

    # method to get the meaning of a word
    def meanings(self, word):
        return Dictionary(word, self.limit).meanings()

    # method to get the synonyms of a word
    def synonyms(self, word):
        return Dictionary(word, self.limit).synonyms()

    # method to get the antonyms of a word
    def antonyms(self, word):
        return Dictionary(word, self.limit).antonyms()


class WordForm:
    # empty constructor
    def __init__(self, word):
        self.word = word
        self.adjective = None
        self.noun = None
        self.verb = None
        self.adverb = None
        # run the method
        self.__word_form()

    def __word_form(self):
        content = get_word_forms(self.word)
        self.adjective = content.get("a")
        self.noun = content.get("n")
        self.verb = content.get("v")
        self.adverb = content.get("r")

    def get_adjective(self, limit=3):
        # check if adjective is a set
        if isinstance(self.adjective, set):
            data = []
            for item in self.adjective:
                data.append(item)
                if len(data) == limit:
                    break
            return data
        else:
            return None

    def get_noun(self, limit=3):
        # check if noun is set
        if isinstance(self.noun, set):
            data = []
            for item in self.noun:
                data.append(item)
                if len(data) == limit:
                    break
            return data
        else:
            return None

    def get_verb(self, limit=3):
        # check if verb is set
        if isinstance(self.verb, set):
            data = []
            for item in self.verb:
                data.append(item)
                if len(data) == limit:
                    break
            return data
        else:
            return None

    def get_adverb(self, limit=3):
        # check if adverb is set
        if isinstance(self.adverb, set):
            data = []
            for item in self.adverb:
                data.append(item)
                if len(data) == limit:
                    break
            return data
        else:
            return None


if __name__ == "__main__":
    # dictionary = DictionaryChecker()
    # print(dictionary.meanings("hello"))
    # print(dictionary.synonyms("hello"))
    # print(dictionary.antonyms("hello"))

    word_form = WordForm("am")
    print(word_form.get_adjective())
    print(word_form.get_noun())
    print(word_form.get_verb())
    print(word_form.get_adverb())
