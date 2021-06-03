# List
# defining list
my_list = [2, 3, 4, 5, 6]
# list comprehension ########################
square_list = [val**2 for val in my_list]
print(square_list)

even_list = [var for var in my_list if var % 2 == 0]
print(even_list)

# set comprehension ########################
numbers = {x for x in range(1, 10)}
print(numbers)

# dictionary comprehension########################
d = {num: num*num for num in range(1, 10)}
print(d)
