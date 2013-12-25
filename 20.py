# Problem 20
# Factorial digit sum
#

def sum_digit(n):
    return sum(int(x) for x in str(n))

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

print sum_digit(fact(100))
