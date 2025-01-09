# def check_3_digits(number):
#     return number in range(100, 1000)

# result = check_3_digits(500)
# print(result)




#pass means nothing
#n consideres every index
# def check_3_digits(list1):
#     for n in list1:
#         if n in range(100,1000):
#             return True
#         else:
#             return False

# result = check_3_digits([55, 99, 6000])
# print((result))


# def check_3_digits(list1):
#     for n in list1:
#         if n in range(100,1000):
#             return True
#         else:
#             pass
        
#     return False


# def check_3_digits(list1):

#     three_digits_list = []

#     for n in list1:
#         if n in range(100,1000):
#             three_digits_list.append(n)
#         else:
#             pass
        
#     return three_digits_list

# result = check_3_digits([555, 99, 600])
# print(result)
# #prints [555, 600]
# #n goes through the arguement and looks at the endexes individually


# #3 things in this list
# coffee_prices = [('cappuccino', 1.5),
#                  ('espresso', 1.2),
#                  ('mocha', 1.9)]

# def most_expensive_coffee(list_of_prices):

#     highest_price = 0
#     my_most_expensive_coffee = ''
# #using coffee and price because coffee_prices has 2 variables
#     for coffee, price in list_of_prices:
#         if price > highest_price:
#             highest_price = price
#             my_most_expensive_coffee = coffee
#         else:
#             pass
    

#     return (my_most_expensive_coffee, highest_price)

# print(most_expensive_coffee(coffee_prices))




# Dynamic Functions Practice #1
# Create a function (all_positives) that returns True if all the values in a list are positive, and False if at least one of the values is negative. Create a list named numbers with positive and negative values.

# Don't call the function, you just need to define it.

#i am defining all posotives and putting it in list 1
def all_positives(list1):
    for n in list1:
        if n >0:
            return True
    #if its seeing if they are more than 0, and if
    #they are it will give me true.
        else:
            pass

results = all_positives((1, 100, 1000))
print (results)
#I am calling the function and printing the results in order to get feedback



# Dynamic Functions Practice #2
# Create a function (sum_less) that adds the numbers of a list as long as they are greater than 0 and less than 1000, and returns the result of said sum. Create a numbers variable, storing a list of numbers so we can test it.

#i am defining sum_less and putting a parameter
def sum_less(number):

    numList = [55, 150, 300]
    added_list = []
  

    for num in numList:
        if num > 0 and num < 100:
            added_list.append(num)

    return added_list

print(added_list(number))




# Dynamic Functions Practice #3
# Create a function (count_even) that counts the number of even numbers that exist in a list (numbers), and returns the result of said count.


#even_num is the parameter
def count_even(even_num):
    
    numbers = [1, 5, 2, 8, 26, 53]
    even_list = []
    total = 0
    for n in numbers:
        if n % 2:
            n = even_list
    for n in even_list:
        total += n

    return even_list

print(count_even(total))


    
