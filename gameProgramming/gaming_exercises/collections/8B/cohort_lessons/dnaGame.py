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

def genRNA(dnaSequence: str) -> tuple:
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

rna = genRNA(dna)
print(rna)

