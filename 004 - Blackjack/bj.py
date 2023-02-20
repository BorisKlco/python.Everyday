import random
import sys
import time


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
        time.sleep(1)
        print("Blackjack!")
        time.sleep(0.5)
        sys.exit("Congratulations, sir! Player won!")
    elif game.score(game.dealer) == ["Blackjack", 21]:
        print(
            f"Dealer: {game.dealer['cards'][0][0]}{game.dealer['cards'][0][1]} {game.dealer['cards'][1][0]}{game.dealer['cards'][1][1]}"
        )
        time.sleep(1)
        print("Blackjack!")
        time.sleep(0.5)
        sys.exit("Dealer won. Sorry, sir.")
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
            print()
            time.sleep(1)
            print("More than 21. Dealer won.")
            time.sleep(1)
            sys.exit("Sorry, sir. Good luck, next time!")
    elif question.lower() == "n":
        game.score(game.dealer)
        if game.score(game.player)[0] > 22:
            player_score = game.score(game.player)[1]
        else:
            player_score = game.score(game.player)[0]
        while True:
            if game.score(game.dealer)[0] > 22:
                dealer_score = game.score(game.dealer)[1]
            else:
                dealer_score = game.score(game.dealer)[0]
            if dealer_score < 22:
                if dealer_score < player_score:
                    dealer_hit = game.hit()
                    game.dealer["cards"].append(dealer_hit)
                    print(f"Card for dealer {dealer_hit[0]}{dealer_hit[1]}")
                    time.sleep(1)
                    game.dealer_print()
                    time.sleep(1)
                    print()
                elif dealer_score == player_score:
                    print()
                    game.dealer_print()
                    time.sleep(0.25)
                    game.player_print()
                    time.sleep(1)
                    sys.exit("Draw!")
                else:
                    print()
                    game.dealer_print()
                    time.sleep(0.25)
                    game.player_print()
                    time.sleep(1)
                    print()
                    print("Dealer won.")
                    sys.exit("Sorry, sir. Good luck, next time!")
            else:
                print("Dealer bust!")
                sys.exit("Congratulations, sir! Player won!")


while True:
    start()
