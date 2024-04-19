# Object-Oriented Programming, Christian Ortiz, v0.0

class Person: # PascalCase for ClassNames
    def  __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.weakness = None
        self.nemesis = None

# To String Function -- How the object appears as a string.
    def __str__(self):
        return f"Name: {self.name}\n This person is {self.age} years old. \nThey weigh {self.weight}  pounds.\n"

    def classFunction(self):
        print("This is an example class function.\n")
        print("It only works when called on an object of that class.")

person1 = Person("Chargoggagoggmanchauggagoggchaubunagungamaugg", 5, 37468.5)
person2 = Person("ChargoggagoggmanchauggagoggchaubunagungamauggChargoggagoggmanchauggagoggchaubunagungamauggesa", 51, 837892.5)
print(person1)
print(person2)

# if person1.weight > person2.weight:
#     print(f"{person1.name} weighs more than {person2.name}.")
# elif person1.weight == person2.weight:
#     print("Each person weighs the same.\n")
# else:
#     print(f"{person2.name} weighs more than {person1.name}.")

# if person1.age < person2.age:
#     print(f"{person1.name} is younger than {person2.name}")

# person1.classFunction()

# Changing properties After Creation
print(person1.name)
person1.name = "goku instinct segregational alliance of the ultimate core crushing scp foundation"
print(person1.name)

# deleting properties -- danger will robinson, DANGER!
# This is does not 'reset' a property, it deletes it completely.
print(person1.name)
del person1.name 
# print(person1)

# deleting objects -- delete them if your finished with them.
del person1

# adding properties to objects
person2.weakness = "dying"
print(person2)
print(person2.weakness)