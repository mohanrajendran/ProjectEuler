# Problem 24
# Lexicographic permuations
#
from math import factorial

output_string = ""
remaining = [str(x) for x in range(10)]
pos = 1000000 - 1
for spot in range(9,-1,-1):
    q = pos / factorial(spot)
    pos = pos % factorial(spot)
    output_string = output_string + remaining[q]
    del remaining[q]

print output_string
