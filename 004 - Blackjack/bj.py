import random
import itertools as it


deck = list(it.product("♠♣♥♦", [str(x) for x in range(2, 11)] + list("JQKA")))
print(deck)
random.shuffle(deck)
print(deck)

cards = [
    (s, v)
    for s in ["H", "S", "C", "D"]
    for v in [str(i) for i in range(2, 11)] + list("JKQA")
]

print(cards)
random.shuffle(cards)
print(cards)
