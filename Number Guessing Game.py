"""
Filename: simple_calculator.py
Author: <Croft, Malakai>
Created: <10/30/2026>
Instructor: Burgess
"""

import random

#prints a random integer between 1 & 100

num = random.randint(1,100)
print(num)

#while
while True:

    x = int(input("Enter your guess: "))
    guess=int(input("enter a number on each attempt"))
    #print(guess)


    if guess < num:
        print("Too low! Try again.")

    elif guess > num:
        print("Too high! Try again.")
    elif guess == num:
        print("Correct! You guessed the number!")
        break
