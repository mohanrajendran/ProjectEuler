# Problem 17
# Number letter counts
#

names = {0:"",
         1:"one",
         2:"two",
         3:"three",
         4:"four",
         5:"five",
         6:"six",
         7:"seven",
         8:"eight",
         9:"nine",
         10:"ten",
         11:"eleven",
         12:"twelve",
         13:"thirteen",
         14:"fourteen",
         15:"fifteen",
         16:"sixteen",
         17:"seventeen",
         18:"eighteen",
         19:"nineteen",
         20:"twenty",
         30:"thirty",
         40:"forty",
         50:"fifty",
         60:"sixty",
         70:"seventy",
         80:"eighty",
         90:"ninety",
         100:"hundred",
         1000:"thousand"
}

def name_len(n):
    return len(name(n).replace(' ',''))

def name(n):
    if n < 20:
        return names[n]
    if n < 100:
        tens = n/10
        units = n%10
        return names[tens*10] + " " + names[units]
    if n < 1000:
        hundreds = n/100
        rem = n%100
        if rem == 0:
            return names[hundreds] + " " + names[100]
        else:
            return name(hundreds*100) + " and " + name(rem)
    if n < 1000000:
        thousands = n/1000
        rem = n%1000
        if rem == 0:
            return names[thousands] + " " + names[1000]
        else:
            return name(thousands*1000) + " and " + name(rem)

l = 0
for i in range(1001):
    l = l + name_len(i)

print l
