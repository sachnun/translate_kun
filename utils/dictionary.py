from pydictionary import Dictionary


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


if __name__ == "__main__":
    dictionary = DictionaryChecker()
    print(dictionary.meanings("hello"))
    print(dictionary.synonyms("hello"))
    print(dictionary.antonyms("hello"))
