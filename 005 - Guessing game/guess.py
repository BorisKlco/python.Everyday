"""
Generate random n 1-100
ask user for difficulty: easy,medium, hard
Lets user guess number, lower num of attempts
"""
import random
import sys


def start():
    """Game start, setting diff level."""
    print("I will think a number 1 to 100, try guess it!")
    print("Pleas choose difficulty: number 1 to 3 (easy, medium and hard)")
    diff = input()
    if diff == "1":
        return 12
    if diff == "2":
        return 8
    if diff == "3":
        return 6
    sys.exit("Not a diff options!")


NUMBER = random.randint(1, 100)
LIFES = start()


def guess(n):
    """Evaluate user number, try again if ValueError."""
    global LIFES, NUMBER
    # print(NUMBER)
    try:
        if int(n) > NUMBER:
            print("Try go lower")
        elif int(n) < NUMBER:
            print("Try go higher")
        else:
            # int(n) == NUMBER:
            sys.exit(f"You won! Number was {NUMBER}")
        print("Lifes left:", LIFES)
        LIFES -= 1
    except ValueError:
        print("Try number 1 to 100")


while True:
    if LIFES > -2:
        guess(input("Guess: "))
    else:
        sys.exit("Out of lifes!")
