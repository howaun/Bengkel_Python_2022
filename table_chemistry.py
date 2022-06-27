#!/usr/bin/env python

import random

def main():
    """Start to guess elements in periodic table of chemistry."""
    print("Guess the common elements!")

    element = [
        "sodium",
        "copper",
        "zinc",
        "silver",
        "carbon",
        "sulfur",
        "uranium",
        "hydrogen",
    ]

    x = random.choice(element)
    print(x)
    guess = None

    while x != guess:

        guess = str(input("What element do you think? Answer : "))

        if x == guess:
            print("You guessed {}. Gotcha!".format(guess))
            break
        else:
            print("You guessed {}. Uh oh...wrong answer".format(guess))

main()