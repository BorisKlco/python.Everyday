import sys


class Bid:
    def __init__(self):
        self.bidLog = {"name": "", "bid": 0}

    def bidding(self, name, bid):
        self.name = name
        self.bid = bid
        if int(self.bid) > self.bidLog["bid"]:
            self.bidLog.update({"name": self.name, "bid": self.bid})

    def winner(self):
        return f'Winner is {self.bidLog["name"]} and his bid is ${self.bidLog["bid"]}'


def ask():
    name = input("Name: ")
    bid = input("bid(only int): ")
    if bid.isnumeric():
        auction.bidding(name, int(bid))
    if input("Someone else? (y/n)").lower() == "y":
        ask()
    else:
        sys.exit(auction.winner())


auction = Bid()
while True:
    ask()
