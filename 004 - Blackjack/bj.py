import random
import sys


class Blackjack:
    def __init__(self) -> None:
        self.cards = [
            (v, s)
            for s in ["♥", "♠", "♣", "♦"]
            for v in [str(i) for i in range(2, 10)] + list("TJKQA")
        ]
        random.shuffle(self.cards)
        self.dealer = {"cards": [self.hit(), self.hit()]}
        self.player = {"cards": [self.hit(), self.hit()]}

    def hit(self):
        """Logic of pulling card from deck"""
        card = self.cards[random.randint(0, len(self.cards) - 1)]
        self.cards.remove(card)
        return card

    def score(self, position):
        value = [0, 0]
        for _, face in enumerate(position["cards"]):
            if face[0] in list("TJKQ"):
                value = [value[0] + 10, value[1] + 10]
            elif face[0] == "A":
                value = [value[0] + 11, value[1] + 1]
            else:
                value = [value[0] + int(face[0]), value[1] + int(face[0])]
        if value in ([21, 11], [11, 21]):
            value = [21, 21]
        return value


game = Blackjack()


def start():
    print(f"Dealer: {game.dealer['cards'][0][0]}{game.dealer['cards'][0][1]} 🃏")
    print("Player: ", end="")
    for _, face in enumerate(game.player["cards"]):
        print(f"{face[0]}{face[1]} ", end="")
    print(
        "Score:",
        game.score(game.player)[0]
        if game.score(game.player)[0] == game.score(game.player)[1]
        else game.score(game.player),
    )
    if game.score(game.dealer) == [21, 21]:
        sys.exit("Blackjack! Dealer won.")
    elif game.score(game.player) == [21, 21]:
        sys.exit("Blackjack! Player won.")
    if input("Hit (y/n)").lower() == "y":
        game.player["cards"].append(game.hit())
        start()
    else:
        pass


while True:
    start()
