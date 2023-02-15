import requests
import sys


class Hangman:
    def __init__(self, word):
        self._word = word
        self._life = 6
        self.hiddenWord = []
        for letter in self._word:
            self.hiddenWord.append("_")

    def hidden(self, letter):
        for position in range(len(self._word)):
            if self._word[position] == letter:
                self.hiddenWord[position] = letter

    def guess(self, letter):
        if self._life > 1:
            if letter in self._word:
                self.hidden(letter)
            else:
                self._life -= 1
        else:
            print("\nWord was", self._word)
            sys.exit("Game over!")

    @property
    def cheater(self):
        print(self._word)

    @property
    def didIwon(self):
        if "_" not in self.hiddenWord:
            sys.exit("You WoN!")

    @property
    def word(self):
        print(f"\nHP left:", self._life)
        print("Word: ", end="")
        for letter in self.hiddenWord:
            print(letter, end=" ")
        print("\n")

    @classmethod
    def start(cls):
        ranWord = requests.get("https://random-word-api.herokuapp.com/word")
        word = ranWord.json()
        return cls(word[0])


game = Hangman.start()
try:
    while True:
        # game.cheater
        game.word
        game.didIwon
        game.guess(input("letter: "))
except KeyboardInterrupt:
    print("\nWord was ", end="")
    game.cheater
    sys.exit("Bye!")
