# Select the secret number from a given range.
# Player must guess the number.
# Compare guess to the secret number.
# What happens if the guess is wrong?
    # Tell them the guess is wrong.
    # Tell them the number of guesses left.
    # Tell them if too high / too low.
# What happens if the guess is right?
    # Tell them if the guess is right.
    # Award a point.
# What happens if the player runs out of guesses?
    # Tell player round has been lost.
    # Award point to CPU.
# Check to see if player or CPU has >= 3 points, if so they win.

import random # Import the random module to our code.

# DECLARATIONS
secretNumber = -1
playerScore = 0
cpuScore = 0
numGuesses = 0
playerName = "borgir"
playerGuess = -1
rangeMin = -1
rangeMax = -1
numAttempts= 3
#Difficultys
difficulty = "easy, hard, scream"

print("""
        *----------------------------*
        |                            |
        |     AWESOME NUMBA GAME!!   |
        |     CHRISTIAN. O           |
        |        2023                |
        |                            |
        *----------------------------*
    
       """)

playerName = input("What should I call you?\nType your name and press enter.\n")
# VERIFY INPUT WHENEVER POSSIBLE
print(f"you want me to call you {playerName}.  Is that correct?")
isCorrect = input("Please type yes if correct, no if not correct.\n")
if isCorrect == "yes":
    print(f"ok {playerName}, let's continue!")
else:
    playerName = input("What should i call you?\nType your name and press enter.\n")

# PLAYER GUESS
print("you need to guess a number from 0 to 20. you have three guesses!\n")

while playerScore != 3 and cpuScore != 3:
    #pass Tells python to skip this block without giving an error.
    secretNumber = random.randint(0, 20) # INCLUSIVE
    #print (secretNumber)
    print(f"player Score: {playerScore}\nCPU Score: {cpuScore}\n")
    numGuesses = 0
    for guesses in range(4):
        print(f"you have {3 - numGuesses} guesses left this round!")
        playerGuess = int(input("Think of your number, type it in and then push ENTER.\n"))
        # int() converts whatever is input into an integer
        print(f"You have picked {playerGuess}. Let's see if your right!\n")
        if playerGuess == secretNumber:
            playerScore += 1
            print("nice job you got it!\n")
            break # immediately exit a loop!
        else:
            if playerGuess < secretNumber:
                print("Too low!\n")
            else:
                print("Too high biggy!\n")
        numGuesses += 1
    if playerGuess != secretNumber:
        cpuScore += 1
        print("The CPU knocked you out this round!\n")

if playerScore >= 3:
    print("You won three rounds, so ya win i guess\n")
else:
    print("Hey scrub you lost, try again nerd\n")

