# Hangman Game by Christian Ortiz, v0.0
import random

words = 'cheese fish ball play girl frog clean salt deep black/ plastic befriend deploy person clicker sargent scissor rockets capsule choir/ determination ultimate-segregation atlas-alliance psuedocode mitochondria systematic-error true-injustice-cosmetology planetary-destruction likeablility super-dimensional-hairspray-hyperdimensional'

# VARIABLE_NAMES in ALL-CAPS ARE CONSTANTS AND NOT MEANT TO CHANGE!
HANGMAN_BOARD = ['''
    +---+
        |
        |
        |
     =======''','''
    +---+
    O   |
        |
        |
     =======''','''
    +---+
    O   |
    |   |
        |
     =======''','''
    +---+
    O   |
   /|   |
        |
     =======''','''
    +---+
    O   |
   /|\  |
        |
     =======''','''
    +---+
    O   |
   /|\  |
   /    |
     =======''',''' 
    +---+
    O   |
   /|\  |
   / \   |
     ======='''] 

# Pick a word from list
def getRandomWord(wordList): # Return a random word from the lsit.
    wordIndex = random.randint(0, len(wordList) - 1) 
    #len(wordlist) - 1 is EXTREMELY COMMON FOR WORKING WITH LISTS.
    return wordList[wordIndex]

i = 0
while i < 100:
    word = getRandomWord(words)
    print(word)
    i += 1


def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_BOARD[len(missedLetters)])
    print()

    print('Missed Letters:', end = ' ')
    for eachLetter in missedLetters:
        print(eachLetter, end = ' ')
    print()

    blanks = '_' * len(secretWord)

    # Replace Blanks with Correct Letter
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:] 

    for letter in blanks:
        print(letter, end = ' ')
    print()
    
def getGuess(alreadyGuessed):
    while True:
        print("Please guess a letter and press enter")
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print("PLease enter a single letter!!!.")
        elif guess in areadyGuessed:
                print('You guessed that already bozo, pick another letter.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz'
                print('Please guess a letter from the english alphabet broseph')
        else:
            return guess

                  
