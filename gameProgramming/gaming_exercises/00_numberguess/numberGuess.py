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
playerName = ""
playerGuess = ""
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

# CPU SECRET NUMBER GENERATION
# Whenever you assign a specific value to something, it's called "hard coded"
secretNumber = random.randint(1 , 10)
secretNumberI = random.randint(1 , 30)
secretNumberII = random.randint(1 , 1000)
print(secretNumber)

print("you need to guess a number from 0 to 20 and you have 3 guesses.\nif you guess it right, you gain a point. if you guess it wrong within all four guesses, CPU gains a point. first to three points win")

# print() an explanation of your three difficulty levels.
#Use input() to store difficulty in difficulty variables.
# assign values to numAttempts, rangeMin, and rangeMax based on choice.


while playerScore != 3 and cpuScore != 3: # START THE MATCH (GAME)
    # Difficulty code needs to be BEFORE the round starts.
    # pass
    print(f"Player Score: {playerScore}.\nCPU Score: {cpuScore}\n")
    numGuesses = 0
    for guesses in range(3):
        print(f"you have {3 - numGuesses} guesses remaining.\n")
        playerGuess = int(input("Type a number from 1 to 20 and press ENTER .\n"))
        # input() will save all data as a STRING by default
        # int() will convert to an INTEGER
        # float() will vonvert to a FLOAT
        print(f"you have chosen {playerGuess}. Let's see if you're right!\n")
    if playerGuess == secretNumber:
        playerScore += 1
        print("woah scrub, you guessed it\n")
        break
    else:
        if playerGuess < secretNumber:
            print("guess higher next time.\n")
        else:
            print("guess lower\n ")
        numGuesses += 1
    if playerGuess != secretNumber:
        cpuScore += 1
        print("The CPU gotcha bud\n")

if playerScore >= 3:
   print("You have won the match\n")
else:
    print("you absolutely suck!") 
            
