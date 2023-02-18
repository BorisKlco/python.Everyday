import random

ccards = [
    (v, s)
    for s in ["♥", "♠", "♣", "♦"]
    for v in [str(i) for i in range(2, 11)] + list("JKQA")
]

# print(cards)
# random.shuffle(cards)
# print(cards)


class Blackjack:
    def __init__(self) -> None:
        self.cards = [
            (v, s)
            for s in ["♥", "♠", "♣", "♦"]
            for v in [str(i) for i in range(2, 11)] + list("JKQA")
        ]

    def pull(self):
        card = random.randint(1, 52)
        print(self.cards[card])
        random.shuffle(self.cards)
        print(self.cards[card])


test = Blackjack()
test.pull()
