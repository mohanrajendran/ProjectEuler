# Problem 15
# Lattice paths
#

import math

def combination(n,k):
    f = math.factorial
    return f(n) / (f(k) * f(n-k))

print combination(40,20)
