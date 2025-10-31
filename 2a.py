import random


target_number = random.randint(1, 9)

while True:
    guess = int(input("Guess a number between 1 and 9: "))
    
    if guess == target_number:
        print("Well guessed!")
        break
    else:
        print("Try again!")
