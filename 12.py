# Problem 12
# Highly divisible triangular number
#

from math import sqrt

prime_list = []
num_div = {}

def generate_primes():
    prime_list.append(2)
    prime_list.append(3)
    count = 2
    cur = 1
    while count <= 10000:
        if cur % 6 == 1:
            cur = cur + 4
        elif cur % 6 == 5:
            cur = cur + 2
        if is_prime(cur):
            prime_list.append(cur)
            count = count + 1

def is_prime(n):
    prime = True
    for prime_num in prime_list:
        if prime_num > sqrt(n) or prime == False:
            break
        if n % prime_num == 0:
            prime = False
    return prime

def num_divisors(num):
    if num in num_div:
        return num_div[num]
    n = num
    div = 1
    while n != 1:
        for prime_num in prime_list:
            if prime_num > n:
                break
            if n % prime_num != 0:
                continue
            cur_div = 1
            while n % prime_num == 0:
                n = n / prime_num
                cur_div = cur_div + 1
            div = div * cur_div
    num_div[num] = div
    return div
    
generate_primes()
n = 1
count = 1
while count <= 500:
    if n % 2 == 1:
        count = num_divisors(n) * num_divisors((n+1)/2)
#        print n, (n+1)/2, num_divisors(n), num_divisors((n+1)/2)
    else:
        count = num_divisors(n/2) * num_divisors(n+1)
#        print n/2, n+1, num_divisors(n/2), num_divisors(n+1)
    n = n + 1
print n*(n-1)/2
