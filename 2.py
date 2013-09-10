# Problem 2
# Even Fibonacci numbers
#

sum = 0
a = 2
b = 8
while a < 4000000:
    sum = sum + a
    a,b = b, a+4*b
print sum
