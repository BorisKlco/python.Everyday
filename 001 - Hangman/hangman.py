import requests
import re


class Hangman:
    def __init__(self, word):
        self.word = word

    def __str__(self):
        return f"{self.word}"

    @classmethod
    def start(cls):
        ranWord = requests.get("https://random-word-api.herokuapp.com/word")
        word = ranWord.json()
        return cls(word[0])


test = Hangman.start()
print(test)

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
