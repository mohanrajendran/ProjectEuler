# Problem 7
# 10001st prime
#

from math import sqrt

def is_prime(n):
    prime = True
    div = 3
    while prime == True and div <= sqrt(n):
        if n % div == 0:
            prime = False
        div = div + 2
    return prime

cur = 1
count = 2
while count <= 10000:
    if cur % 6 == 1:
        cur = cur + 4
    elif cur % 6 == 5:
        cur = cur + 2
    if is_prime(cur):
        count = count + 1
print cur
