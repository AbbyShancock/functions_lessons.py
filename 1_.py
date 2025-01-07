from determineEligibility import determineEligibility_toGraduate, listOfMovies
# #functions are always to wrap up your code
# #into reusable units

# #define a function with def
# #function names end in ()
# #when I pass in a parameter,
# #i am passing in a placeholder
# #for future information (name)


def say_hello(name,age,address):
    print(f"Hello!{name}")
    print(f"How are you?{name}")
    print(f"{name} are {age} years old")
    print(f"{name} loves in {address}")

# #call the function
# #pass in information called arguement (Alice)
#     #pass a second arguement for age
#     #pass a third arguemnet for address
#     #three parameters, three arguements.


say_hello("Alice",22,"123 Main St.") 
say_hello("Paul",34, "456 Main St")
say_hello("Bob",56,"789 Main St")
say_hello("Altair",45,"101 Main St")



determineEligibility_toGraduate("Alice", 120, 2.0, 800)
determineEligibility_toGraduate("Bob", 119, 1.9, 799)

listOfMovies("the Matrix", 10, "action")
listOfMovies("The Hangover", 5, "comedy")





#the return statement is
#used to return a value from a function
#return statements are unsed to end a function and
#send a result back to the caller

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))
