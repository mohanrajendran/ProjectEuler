# Problem 23
# Non-abundant sums
#

def d(n):
    s = 0
    for i in range(1,n/2+1):
        if n%i == 0:
            s = s + i

    return s

abundant_number = [n for n in range(28123) if d(n) > n]
ab_sum = [False for x in range(28123)]
tot_sum = 28122*28123/2
for i in range(len(abundant_number)):
    for j in range(i,len(abundant_number)):
        ai = abundant_number[i]
        aj = abundant_number[j]
        s = ai + aj
        if s >= 28123:
            break
        if ab_sum[s] == False:
            ab_sum[s] = True
            tot_sum = tot_sum - s

print tot_sum
