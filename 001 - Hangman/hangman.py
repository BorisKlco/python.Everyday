import requests
import re


def getWord():
    ranWord = requests.get("https://random-word-api.herokuapp.com/word")
    return ranWord.json()


while True:
    test = []
    word = getWord()
    for letter in word[0]:
        test.append(letter)

    # guess = input("Guess letter: ").lower()
    # if len(guess) == 1:
    #     if re.match(r"[a-z]", guess):
    #         print(guess)
    #         print(test)
    #     else:
    #         print("Only a-z")
    # else:
    #     print("Only one letter")
