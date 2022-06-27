#!/usr/bin/env python

import random

def main():
    """Hi!! Lets start a Priodic Elements guessing game."""
    print("Guess the Elements!")

    Chemy = [
        "Li",
        "Al",
        "Mg",
        "K",
        "H",
        "O",
        "I"
        ]

    x = random.choice(Chemy)
    # print(x)
    guess = None

    while x != guess:

        guess = str(input("What elements am I thinking of? "))
        
        if x == guess:
            print("You guessed {}. Congratulations you got it right!".format(guess))
            break
        else:
            print("You guessed {}. Unfortunately you got the wrong answer. Please try again!".format(guess))

main()