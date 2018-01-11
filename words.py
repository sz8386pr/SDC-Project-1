# Created by Scott Kim
# This file holds the Words class (str(words to guess), int[Character counts of each words])

class Words:

    def __init__(self, word, charCount):
        self.word = word
        self.charCount = charCount

    def get_word(self):
        return self.word

    def get_char_count(self):
        return self.charCount

    def __str__(self):
        return self.word
