"""
Game: Blackjack
Generating 52 cards --> picking cards from deck to deal and removing tham from array.
Storing final value of cards in var for player/dealer.
"""
import random


class Blackjack:
    def __init__(self) -> None:
        self.cards = [
            (v, s)
            for s in ["♥", "♠", "♣", "♦"]
            for v in [str(i) for i in range(2, 11)] + list("JKQA")
        ]
        self.score = 0
        self.score_ace = 0
        self.dealer = 0
        self.dealer_ace = 0

    def hit(self):
        """Logic of pulling card from deck"""
        random.shuffle(self.cards)
        card = self.cards[random.randint(0, len(self.cards) - 1)]
        self.cards.remove(card)
        return card


game = Blackjack()
