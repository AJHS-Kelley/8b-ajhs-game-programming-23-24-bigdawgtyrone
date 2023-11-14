# Example Game Functions project, Christian ortiz, v0.0
import random
punchPower = ''
punchSpeed = ''
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
    if power >= 9 and speed >= 6 and target == head:
        knockDown = True
        knockOut = True
    print('You landed a perfect punch and knocked your opponent out!')
    elif power >= 7 and speed >= 6 and target == head:
        knockDown = True
        print('You have knocked your opponent down!')
    else
        knockdown = False
        print('You did not land your power punch.')
        pass

    
    
    print('Where do you want to hit your opponent?\n')
powerPunch = input('Type "head" or "body" then press Enter')

if powerPunch == "head":
    punchPower = random.randint(1, 10)
    punchSpeed = random.randint(1, 10) 
    print('You swung for your opponents head')
    print('This is your punch power -->' + punchPower)
    print('This is your punch speed -->' + punchSpeed)

