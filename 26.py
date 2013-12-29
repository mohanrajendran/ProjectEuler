# Problem 26
# Reciprocal cycles
#

def rec_cycle(n):
    rem = []
    cycle_found = False
    curnum = 1
    while cycle_found == False:
        while curnum < n:
            curnum = curnum * 10
        curnum = curnum % n
        if curnum not in rem:
            rem.append(curnum)
        else:
            rem.append(curnum)
            cycle_found = True
        if curnum == 0:
            cycle_found = True

    final_term = rem[-1];
    if final_term == 0:
        return 0
    starting_term = rem.index(final_term)
    cycle_length = 0
    for i in range(starting_term, len(rem)-1):
        curnum = rem[i]
        while curnum < n:
            curnum = curnum* 10
            cycle_length = cycle_length + 1        

    return cycle_length

longest_cycle = 0
longest_number = 0
for i in range(1,1000):
    c = rec_cycle(i)
    if c > longest_cycle:
        longest_cycle = c
        longest_number = i

print longest_number
