# Problem 19
# Counting Sundays
#

count = 0
start = 2 # 1 Jan 1901 was a Tuesday

for year in range(1901,2001):
    for month in range(1,13):
        if start == 0:
            count = count + 1
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            start = (start + 31) % 7
        elif month == 2:
            if year % 4 == 0:
                start = (start + 29) % 7
            else:
                start = (start + 28) % 7
        else:
            start = (start + 30) % 7

print count
