# Problem 34
# Digit factorials
#

fact = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

def is_curious(n):
    m = n

    s = 0
    while n != 0:
        s = s + fact[n%10]
        n = n / 10

    return m == s

s = 0
for i in range(3,6*fact[9]):
    if is_curious(i):
        s = s + i

print s
