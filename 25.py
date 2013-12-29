# Problem 25
# 1000-digit Fibonacci number
#

(a, b, c) = (0, 1, 1)
while len(str(b)) < 1000:
    (a, b, c) = (b, a + b, c+1)

print c
