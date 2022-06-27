#!/usr/bin/env python

import random

def main():
    """Start a number guessing game between 1 - 100."""
    print("Guess the number!")

    x = random.betavariate(1, 100)
    print(x)
    guess = None

    while x != guess:

        guess = int(input("Pick a number between 1 to 100: "))

        if x == guess:
            print("You genius!")
        else:
            print("Try guess again.")
        

main()