# eval() len() factorial() sort()

x = 3
print(eval('x**2+2*x-2'))

#number items
numbers = [4,76,2,34,12,9]
print(len(numbers))

#factorial() math module factorial of a number without writing the whole code
import math
print(math.factorial(5))

print(math.factorial(9))

#sort() sorts the elements of an object in a specified ascending or descending order
numbers2 = [4,76,2,34,12,9]
numbers2.sort(reverse=True)
print(numbers2)
numbers2.sort(reverse=False)
print(numbers2)