# Example Game Functions project, Christian ortiz, v0.0
import random
punchPower = ''
punchSpeed = ''
target = ''
health = 200
target = ''
def functionOne():
    pass

def functionTwo(param1):
    pass

def functionThree(param1 = "Default Value"):
    pass

def functionFour(param1, param2, param3):
    pass

def powerPunch(speed, power, target):
    if power >= 9 and speed >= 9 and target == head:
        knockDown = True
        knockOut = True
        print('You landed a perfect punch and knocked your opponent out!')
    elif power >= 9 and speed >= 7 and target == head:
        knockDown = True
        print('You have knocked your opponent down!')
    else:
        knockDown = False
        print('You did not land your power punch.')


playerName = input("What's your fighter name?\nType it here then press enter.\n")
print(f"you want to be called {playerName}.  that Right?")
isCorrect = input("Please type yes if correct, no if not correct.\n")
if isCorrect == "yes": 
    print(f"ok {playerName}, let's get started\n")
else:
    playerName = input("what's your fighter name?\nType your name then press enter.\n")

print('Where do you want to hit your opponent?\n')
powerPunch = input('Type "head" or "body" then press Enter\n')
    

if powerPunch == "head":
    punchPower = random.randint(1, 10)
    punchSpeed = random.randint(1, 10)
    print('You swung for your opponents head')
    print(f'This is your punch power--> {punchPower}')
    print(f'This is your punch speed--> {punchSpeed}')
    print('This is your opponents current health')
    health = health - punchPower * punchSpeed
    print(health)
    print("It's now your opponents turn")
elif powerPunch == 'body':
    punchPower = random.randint(1, 10)
    punchSpeed = random.randint(1, 10)
    print('You threw a shot at your opponents body')
    print(f'This is your punch power--> {punchPower}')
    print(f'This is your punch speed--> {punchSpeed}')
    print('This is your opponents current health')
    health = health - punchPower * punchSpeed
    print(health)
    print("It's now your opponents turn")
else:
    print('You didnt commit to the punch and threw a low blow')
    print('This is your opponents current health')
    print(health)
    print("It's now your opponents turn")