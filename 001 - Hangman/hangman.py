import requests
import re


class Hangman:
    def __init__(self, word):
        self._word = word
        self._life = 6
        self.hiddenWord = []
        for letter in self._word:
            self.hiddenWord.append("_")

    def __str__(self):
        return f"{self._word}"

    def hidden(self, letter):
        for position in range(len(self._word)):
            if self._word[position] == letter:
                self.hiddenWord[position] = letter

    def guess(self, letter):
        if letter in self._word:
            self.hidden(letter)
            print(letter)
            print(self._word)
            print(self.hiddenWord)
        else:
            print("nope")
            print(self._word)

    @classmethod
    def start(cls):
        ranWord = requests.get("https://random-word-api.herokuapp.com/word")
        word = ranWord.json()
        return cls(word[0])


test = Hangman.start()
while True:
    test.guess(input("letter: "))

# while True:
#     test = []
#     word = getWord()
#     for letter in word[0]:
#         print(letter)

# guess = input("Guess letter: ").lower()
# if len(guess) == 1:
#     if re.match(r"[a-z]", guess):
#         print(guess)
#         print(test)
#     else:
#         print("Only a-z")
# else:
#     print("Only one letter")


# Hidden --> take input letter --> find it in "word" --> take "letter" location in "word" --> replace hidden["_"] with user "letter"
