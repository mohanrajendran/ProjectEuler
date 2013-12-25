# Problem 15
# Lattice paths
#

def combination(n,k):
    return fact(n) / (fact(k) * fact(n-k))

def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

print combination(40,20)
