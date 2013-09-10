# Problem 3
# Largest prime factor
#

from math import sqrt

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n == 3:
        return True
    else:
        prime = True
        div = 3
        while prime == True and div <= sqrt(n):
            if n % div == 0:
                prime = False
            div = div + 2
        return prime

big_num = 600851475143
max_factor = 2
div = 3
while div <= sqrt(big_num):
    if big_num % div == 0 and  is_prime(div):
        max_factor = div
    if div == 3:
        div = 5
    elif div % 6 == 1:
        div = div + 4
    elif div % 6 == 5:
        div = div + 2
print max_factor
