# Problem 5
# Smallest multiple
#

# Euclidean algorithm(a > b)
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

p = 2520
for i in range(11,21):
    g = gcd(p, i)
    p = p * i / g
print p
