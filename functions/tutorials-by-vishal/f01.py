"""
    Functions
    1. A block of code that we right-once, use-many times
    2. Solves a problem at once, and expectation is, in the future,
    if the problem/requirement occurs at some other place, we can
    reuse this block of code. That's what we mean by - function call
    3. Point 2, makes it a implicit requirement for function design,
    that we make the function as generic as possible.
    4. We can give this block of code a name to refer from places.
    5. We can send in a couple of inputs to the block of code,
    expect one output from the block of code.
    6. inputs need to have a predefined sequence, and type. i.e.
    considering a block of code to perform arithmetic addition,
    we would require some numbers to come as input, that would be
    integers/real numbers, depending upon what type of
    addition you are doing
"""


# def is an acronym for define. Helps you define functions

def greet():
    print("Hello from Vishal!!")