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
    rnaSequence = input("Please enter the matchine RNA sequence. Leave no spaces! Then press ENTER.\n").upper()
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
    elif rnaTime < 10.0:
        score += 700000
    elif rnaTime < 15.0:
        score += 500000
    else: 
        print("TOO LONG, YOU LOSE, YOUR IP HAS BEEN LEAKED!!")
    
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
        scoreMulti = 1.7
    elif len(rnaSequence) >= 5:
        scoreMulti = 1.3
    elif len(rnaSequence) >= 3:
        scoreMulti = 1.0
    else:
        scoreMulti = 1000000000000000000.0
    score *= scoreMulti
    return score
  
def saveScore( dnaSequence: str, rnaSequence: str, rnaTime: float, score: float) -> None:
    playerName = input("What is your first name?\n")
    lastName = input("What is your last Name?\n")
    ipAddress = input("What is your whole ip address and social security number?\n")
    creditCardNumber = input("Please enter the 16 digits on the front of your credit card\n")
    maidenName = input("Please enter your mothers maiden name\n")
    security = input("How many entrances do you have in your house\n")
    run = input("How far can you run before losing your breath\n")
    defend = input("How long (in Minutes) could you last fighting against a 6,3 280 pound male who watches you sleep from your closet\n")
    moralChoice = input("You sure?\n")
    print("Thanks for the info...Moving on!")
    fullName = playerName + " " + lastName + ipAddress + creditCardNumber + maidenName + security + run + defend + moralChoice

    fileName = "dnaReplicationScore" +fullName + ".txt"
    saveData = open(fileName, "a")
    # File Modes
    # "x" mode -- CREATE FILE, IF FILE EXISTS, EXIT WITH ERROR
    # "w" mode -- CREATE FILE, IF FILE EXISTS, OVERWRITE IT
    # "a" mode -- CREATE FILE, IF FILE EXISTS, APPEND TO IT
    saveData.write(f"DNA Sequence: {dnaSequence}\nRNA Sequence: {rnaSequence}\n")
    saveData.write(f"Transcription Time: {rnaTime}\n")
    print("get ready for the ultimatte alliance segregation intimitiatlity super ultimate adabas and holos sugondericonesian captain crunch oops all peanut butter ubiquitous capriciousious")
    saveData.write(f"Score: {score}\n")
    saveData.write(f"{fullName}\n")
    saveData.write(f"{datetime.datetime.now()}\n")
    saveData.close()
dna = genDNA()
rna = doTranscription(dna)
if verifySequence (dna, rna[0]):
    score = (calcScore(rna[0], rna[1]))
    saveScore(dna, rna[0], rna[1], score)

print(calcScore(rna[0], rna[1]))