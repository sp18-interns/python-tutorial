"""
    1. What is OOP?
    2. Why do you need OOP?
    3. What is/are the fundamental building block/s of OOP?
    4. How would one implement OOP?
    5. What is available in opposition to OOP?
"""


# built-in datatypes
# int
# float
# str
# bool
# tuple
# list - mutable/dynamic
# set - mutable/dynamic
# dict - mutable/dynamic
# pizza - mutable/dynamic - has support to contain - int/float/etc, all existing datatypes.
# and it also gives us support to associate behaviour of pizza

# TODO: Mukesh to read on the difference between break and pass and return and explain us.

# Rubber Stamp
class Pizza:
    # purpose of this function is to initialize the object with some default attributes & behaviours.
    def __init__(self, name, size, is_veg, toppings, base, price):
        # Assume all the parameters are being set as pizza attributes
        print(f"self: {self}")
        self.name = name
        self.size = size
        self.is_veg = is_veg
        self.toppings = toppings
        self.base = base
        self.price = price

    def get_size(self):
        return self.size

    # purpose of this function is to delete/remove or at least mark the object "to be deleted".
    def __del__(self):
        pass

    def __str__(self):
        return f""" *****************************
name: {self.name}
size: {self.size}
base: {self.base}
is veg: {self.is_veg}
toppings: {self.toppings}
price: {self.price}"""


# Create an imprint. Here margherita is an imprint of the Rubber Stamp named Pizza
margherita = Pizza("Margherita", 7.00, True, ["Pineapple", "Jalapenos"], "Cheese Burst", 195.5)
print(f"margherita: {margherita}")
print(f"margherita's size: {margherita.get_size()}")

farmhouse = Pizza("Farmhouse", 12.00, False, ["Cheese", ], "Cheese Burst", 350)
print(f"farmhouse: {farmhouse}")

""" noun verb?
TODO: Vishal to read about it.

++++++++++++++++++++++++++++++++
PizzaContainer:
    attributes: name, size, is_veg, toppings, base, price
    behaviours:
        - to select a base
        - to add toppings
        - to name the pizza
        - to calculate the price based on the base, toppings
            & size of the pizza
        - to be able to pack the pizza in a box
        - to be able to decide whether the pizza
            is veg/non-veg
"""
