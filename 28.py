# Problem 28
# Number spiral diagonals
#

s = 1
curnum = 1
inc = 2
for i in range(500):
    for j in range(4):
        curnum = curnum + inc
        s = s + curnum
    inc = inc + 2

print s
