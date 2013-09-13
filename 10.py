# Problem 10
# Summation of primes
#

# Solution using the Sieve of Eratosthenes

sum = 0
target = 2000000
sieve = [True] * target
sieve[0] = False
sieve[1] = False
sieve[2] = True

for i in range(1,target):
    if sieve[i] == False:
        continue
    else:
        for j in range(i*i,target,i):
            sieve[j] = False

for i in range(1,target):
    if sieve[i]:
        sum = sum + i

print sum
