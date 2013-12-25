# Problem 21
# Amicable numbers
#

div_sum = {}

def d(n):
    if n in div_sum:
        return div_sum[n]
    
    s = 0
    for i in range(1,n/2+1):
        if n % i == 0:
            s = s + i

    div_sum[n] = s
    return s

s = 0
for i in range(1,10001):
    if (d(d(i))) == i and d(i) < 10001 and d(i) != i:
        s = s + i

print s
