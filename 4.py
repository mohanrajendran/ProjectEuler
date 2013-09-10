# Problem 4
# Largest palindrome product
#

def is_palin(n):
    if n < 10:
        return True
    rev = 0
    orig = n
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    if rev == orig:
        return True
    else:
        return False

largest_palin = 0
for i in range(999,99,-1):
    if i % 11 == 0:
        s = i
        inc = -1
    else:
        s = (i//11)*11
        inc = -11
    for j in  range(s,99,inc):
        p = i * j
        if is_palin(p) and p > largest_palin:
            largest_palin = p

print largest_palin
