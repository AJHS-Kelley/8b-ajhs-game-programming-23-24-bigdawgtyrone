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