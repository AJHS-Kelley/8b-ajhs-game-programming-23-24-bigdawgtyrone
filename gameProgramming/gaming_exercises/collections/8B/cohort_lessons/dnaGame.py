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
print(dna)