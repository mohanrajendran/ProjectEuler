# Problem 30
# Digit fifth powers
#

def power_sum(n):
    m = n
    s = 0
    while n > 0:
        c = n % 10
        s = s + c**5
        if s > m:
            return m - 1
        n = n / 10

    return s

s = 0
# This number limit is generated as follows, assume a 7-digit
# number, maximum sum of powers = 7*9**5 = 413343 < 1000000
# Thus, condition does not hold true for all numbers above
# at most 1000000. For a little bit more rigor,
# stop at 6*9**5 = 354294
for i in range(2,354294):
    if power_sum(i) == i:
        s = s + i

print s
