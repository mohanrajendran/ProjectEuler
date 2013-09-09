# Problem 1
# Multiples of 3 and 5
#

def is_multiple(n):
    return (n%3 == 0 or n%5 == 0)

sum = 0
for i in range(1000):
    if is_multiple(i):
        sum = sum + i
print sum
