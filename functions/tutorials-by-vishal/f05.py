# greeter is the person who is greeting
# person_being_greeted is the person who is being greeted
# the function creates a formatted string greeting and returns
# that back to the caller

# The function signature signifies -
# 1. The name of the function
# 2. The input parameters for the function
# 3. The return from the function

def welcome(welcome_greeting):
    welcome_message = f"""
{welcome_greeting}. Please complete the below listed formalities
1. collect id card from reception
2. create an internet usage id
3. request a desk allocation
4. connect with your team leader
"""
    return welcome_message
