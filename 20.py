# Problem 20
# Factorial digit sum
#

from math import factorial

def sum_digit(n):
    return sum(int(x) for x in str(n))

print sum_digit(factorial(100))
