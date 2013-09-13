# Problem 9
# Special Pythagorean triplet
#

def gcd(a,b):
    if b > a:
        gcd(b,a)
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

# Euclid's formula for primitive Pythagorean triplets
# a^2 + b^2 = c^2 where a = m^2 - n^2
# b = 2mn  and  c = m^2 + n^2, (m,n) are integers
# m>n, m-n is odd and gcd(m,n) = 1

target = 1000
found = False

for m in range(1000):
    if m%2 == 0:
        for n in range(1,m,2):
            if gcd(m,n) != 1:
                continue
            s = 2*m*(m+n)
            if target%s == 0:
                found = True
                a = m**2 - n**2
                b = 2*m*n
                c = m**2 + n**2
                break
    else:
        for n in range(2,m,2):
            if gcd(m,n) != 1:
                continue
            s = 2*m*(m+n)
            if target%s == 0:
                found = True
                a = m**2 - n**2
                b = 2*m*n
                c = m**2 + n**2
                break
    if found:
        break

ap = a*target/s
bp = b*target/s
cp = c*target/s
print ap*bp*cp
