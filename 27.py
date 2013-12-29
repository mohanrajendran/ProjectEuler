# Problem 27
# Quadractic primes
#

from math import *

primes = []
def generate_primes(n):
    primes.append(2)
    primes.append(3)

    curnum = 5
    while curnum < n:
        for num in primes:
            if(num > sqrt(curnum)):
                primes.append(curnum)
                break
            if(curnum % num == 0):
                break
        if curnum % 6 == 5:
            curnum = curnum + 2
        else:
            curnum = curnum + 4

def prime_count(a,b):
    n = 0
    while True:
        curnum = n*n + a*n + b
        if curnum < 0 or curnum not in primes:
            break
        n = n + 1
    return n

generate_primes(2000000)
longest_prime_count = 0
prod = 0
for a in range(-999,1000,2):
    for b in primes:
        if b >= 1000:
            break
        p = prime_count(a,b)
        if p > longest_prime_count:
            longest_prime_count = p
            prod = a * b

print prod
