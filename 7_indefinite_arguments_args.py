#args + allows you to pass multiple non-key arguements
#**kwargs +allows you to pass multiple keyword-arguements
#               *unpacking operator
#      1. positional   2. default   3. keyword   4. arbitrary


#args


def add(*args):
    total = 0
    for arg in args:
        total += args
    return total

print(add (1, 2, 3))



def display_name(*args):
    for arg in args:
        print(arg, end =" ")

display_name("Spongebob", "Harold", "Squarepants")
# the " " is in between them, each arg ends in " "


#kwargs


def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street ="123 fake st.", city = "Detroit", state = "MI", zip="54321")
#prints:
# street: 123 fake st.
# city: Detroit
# state: MI
# zip: 54321




# Indefinite Arguments (*args) Practice #1
# Create a function called sum_squares that takes any number of numeric arguments, and returns the sum of their values squared.

# For example for the arguments sum_squares(1,2,3) it should return 14 (1+4+9).


# Indefinite Arguments (*args) Practice #2
# Create a function called absolute_sum, which takes any number of arguments, and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together, in other words, considers them all - negative and positive - as positive).

# Indefinite Arguments (*args) Practice #3
# Create a function called personal_numbers that receives, as its first argument, a name, and then an indefinite number of values.

# The function should return the following message:

# "{name}, the sum of your numbers is {sum_numbers}"
