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
            value = ["Blackjack", 21]
        return value

    def player_print(self):
        print("Player: ", end="")
        for _, face in enumerate(self.player["cards"]):
            print(f"{face[0]}{face[1]} ", end="")
        print(
            "Score:",
            self.score(self.player)[0]
            if self.score(self.player)[0] == self.score(self.player)[1]
            else self.score(self.player),
        )

    def dealer_print(self):
        print("Delear: ", end="")
        for _, face in enumerate(self.dealer["cards"]):
            print(f"{face[0]}{face[1]} ", end="")
        print(
            "Score:",
            self.score(self.dealer)[0]
            if self.score(self.dealer)[0] == self.score(self.dealer)[1]
            else self.score(self.dealer),
        )


game = Blackjack()


def start():
    print(f"Dealer: {game.dealer['cards'][0][0]}{game.dealer['cards'][0][1]} 🃏")
    game.player_print()
    print()
    if game.score(game.player) == ["Blackjack", 21]:
        sys.exit("Blackjack! Player won.")
    elif game.score(game.dealer) == ["Blackjack", 21]:
        print(
            f"Dealer: {game.dealer['cards'][0][0]}{game.dealer['cards'][0][1]} {game.dealer['cards'][1][0]}{game.dealer['cards'][1][1]}"
        )
        sys.exit("Blackjack! Dealer won.")
    question = input("Hit (y/n)? ")
    if question.lower() == "y":
        next_card = game.hit()
        print(f"{next_card[0]}{next_card[1]} , sir!")
        print()
        game.player["cards"].append(next_card)
        if game.score(game.player)[1] < 22:
            start()
        else:
            game.player_print()
            sys.exit("More than 21, sorry.")
    elif question.lower() == "n":
        # game.dealer_print()

        # while game.score(game.dealer)[1] < game.score(game.player)[1]:
        #     dealer_hit = game.hit()
        #     print(f"Card for dealer: {dealer_hit[0]}{dealer_hit[1]}")
        #     game.dealer["cards"].append(dealer_hit)

        if game.score(game.dealer)[1] > 21:
            game.dealer_print()
            sys.exit("Dealer more than 21, Cg, you won!")
        elif game.score(game.dealer)[1] < game.score(game.player)[1]:
            game.player_print()
            game.dealer_print()
            sys.exit("Dealer won, sorry")

        # sys.exit("More than 21, sorry.")


while True:
    start()
