#CS 21
#Random Number Generator Program

import random

num = random.randint(1,100)

MAX_TRIES = 5 
tries = 0

again = "y"
while again == "y" or again == "Y":
    
    print("I am thinking of a number between 1 and 100")
    print("You have 5 tries to guess it. Goodluck!")

    guess = int(input("Enter a guess between 1 and 100: "))
    
    while guess > 100 or guess < 1:
        print("Invalid input")
        guess = int(input("Enter a guess: "))
               
    while num != guess and (tries + 1) < MAX_TRIES:    
        if guess > num:
            print("Too high")
            tries += 1
            guess = int(input("Enter a guess: "))
        elif guess < num:
            print("Too low")
            tries += 1
            guess = int(input("Enter a guess: "))
        
    if num != guess:
        print("Sorry, you're out of tries. The number was ", num, ".", sep="")
    else:
        print("Congratulations! You guessed it in", tries+1, "tries.")

    again = input("Play again? (Y or N)")
