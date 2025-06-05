"""
A Narcissistic Number (or Armstrong Number) is a positive number which is the sum of its own digits, 
each raised to the power of the number of digits in a given base. 
In this Kata, we will restrict ourselves to decimal (base 10).
"""


def narcissistic(value):
	return sum([int(x) ** len(str(value)) for x in str(value)]) == value


print(narcissistic(153)) # True
print(narcissistic(1652)) # False