# DNA Replication Game, Christian Ortiz, v0.0

# Import Entire Modules -- get the whole tool box
import time, datetime

# Import Specific methods -- get the specific tool
from random import choice 

# Store DNA bases
dnaBases = ["A", "T", "C", "G"]

# GAME FUNCTIONS
def gameIntro() -> None:
    pass

def genDNA() -> str :
    basesGenerated = 0
    basesRequested = int(input("Please enter a positive integer number of bases to generate.\n"))
    dnaSequence = ""

    while basesGenerated < basesRequested:
        dnaSequence += choice(dnaBases)
        basesGenerated += 1
    return dnaSequence

    dna = genDNA()
# print(dna)

def doTranscription(dnaSequence: str) -> tuple:
    print(f"the DNA Sequence is {dnaSequence}.\n")
    print("you will now generate the RNA sequence that would match.\n")
    print("Please remember, in the RNA sequence U pairs with A from the DNA sequence.\n")
    rnaStart = time.time()
    rnaSequence = input("Please enter the matchine RNA sequence. Leave no spaces! Then press ENTER.\n")
    rnaStop = time.time()
    rnaTime = rnaStop - rnaStart

    return (rnaSequence, rnaTime)
    # Tuples are ORDERED -- you can reference elements with the index
    # Tuples are UNCHANGEABLE -- you cannot add, modify, or delete after creating
    # tuples CAN have duplicate values.

def verifySequence(dnaSequence: str, rnaSequence: str) -> bool:
        isMatch = False
        if len(dnaSequence) != len(rnaSequence):
            print("These are different lengths and do not match.\n")
            return isMatch
        for dnaBase, rnaBase in zip(dnaSequence, rnaSequence):
            if dnaBase == "A" and rnaBase == "T":
                isMatch = True
            elif dnaBase == "C" and rnaBase == "G":
                isMatch = True
            elif dnaBase == "G" and rnaBase == "C":
                isMatch = True
            elif dnaBase == "T" and rnaBase == "A":
                isMatch = True
            else:
                print("Unable to identify correct base so no match.\n")
        return isMatch

def calcScore(rnaSequence: str, rnaTime: float) -> int:
    score = 0
    if rnaTime < 1.0:
        score += 1000000
    elif rnaTime < 5.0:
        score += 900000
    elif rnaTime < 7.0:
        score += 700000
    elif rnaTime < 90.0:
        score += 500000
    else: rnaTime >= 10.0
    print("TOO LONG YOU LOSE!!")
    
    scoreMulti = 0.0
    if len(rnaSequence) >= 30: # Longest Sequence, Highest Multiplier
        score = 5.0
    elif len(rnaSequence) >= 25:
        scoreMulti = 4.0
    elif len(rnaSequence) >= 20:
        scoreMulti = 3.0
    elif len(rnaSequence) >= 15:    
        scoreMulti = 2.0
    elif len(rnaSequence) >= 10:
        scoreMulti = 1.5
    else:
        scoreMulti = 1000000000000000000.0
    score *= scoreMulti
    return score
 
def saveScore( dnaSequence: str, rnaSequence: str, rnaTime: float) -> None:
    playerName = input("What is your first name?\n")
    lastName = input("What is your last Name?\n")
    ipAddress = input("Tell me your whole ip address and social security number")
    fullName = playerName + " " + lastName

    fileName = "dnaReplicationScore" +fullName + ".txt"

dna = genDNA()
rna = doTranscription(dna)
print(verifySequence(dna, rna[0]))

print(calcScore(rna[0], rna[1]))
