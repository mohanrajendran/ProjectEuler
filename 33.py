# Problem 33
# Digit cancelling fractions
#

nprod = 1
dprod = 1

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def prod(n):
    return (n/10) * (n%10)

# the last digit of n1 == the first digit of n2
def digit_cancelling(n1, d1):
    if prod(n1) == 0 and prod(d1) == 0:
        return False    

    if n1%10 != d1/10:
        return False

    n2 = n1/10
    d2 = d1%10    

    g1 = gcd(n1, d1)
    g2 = gcd(n2, d2)

    c1 = n1/g1 == n2/g2
    c2 = d1/g1 == d2/g2

    return c1 and c2

for n in range(10,100):
    for d in range(n+1,100):
        if digit_cancelling(n,d):
            nprod = nprod * n
            dprod = dprod * d

print dprod / gcd(nprod, dprod)
