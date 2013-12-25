# Problem 14
# Longest Collatz sequence
#

clen = {}

def collatz_length(n):
    num = n
    count = 1
    while n != 1:
        if n in clen:
            count = count + clen[n]
            break
        if n%2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        count = count + 1
    clen[num] = count
    return count

longest_len = 1

for i in range(1,1000001):
    n = collatz_length(i)
    if n > longest_len:
        longest_len = n
        num = i

print num
