import f01
import f02
import f03
import f04
import f05
import f06
"""
    The purpose of this file is just to be used a testing ground for all your
    experiments or tutorials on functions
"""

# nothing is being given back or returned here. Just the block of code is being called without inputs.

print("Calling greet() from f01")
f01.greet()
print('***************************************')
print("Calling greet(name) from f02")

# Shuklaji here is known as a function argument

f02.greet("Shuklaji")
print('***************************************')

print("Calling greet(greeter, person_being_greeted) from f03")

# Mishraji here is the person_being_greeted, and Vishal here is the greeter

f03.greet("Vishal", "Mishraji")

print('***************************************')

print("Calling greet(greeter, person_being_greeted) from f04")

# Mishraji here is the person_being_greeted, and Vishal here is the greeter

# greeting = f04.greet("Vishal", "Mishraji")
# print(greeting)

print('***************************************')

print("Calling welcome(welcome_greeting) from f05")

# Mishraji here is the person_being_greeted, and Vishal here is the greeter

# response = f05.welcome(f04.greet("Vishal", "Mishraji"))
print(f05.welcome(f04.greet(person_being_greeted="Mishraji", greeter="Vishal")))

print('***************************************')

print("Calling welcome(welcome_greeting) without welcome_greeting from f06")

print(f06.welcome())
