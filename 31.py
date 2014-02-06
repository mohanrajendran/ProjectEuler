# Problem 31
# Coin sums
#

ways = [[-1 for i in range(8)] for j in range(201)]
size = [1, 2, 5, 10, 20, 50, 100, 200]

def num_ways(amount, coins):
    if ways[amount][coins] != -1:
        return ways[amount][coins]

    if amount == 0:
        return 1

    ways[amount][coins] = 0
    for i in range(coins+1):
        left = amount - size[i]
        if left < 0:
            continue

        ways[amount][coins] = ways[amount][coins] + num_ways(left, i)
        

    return ways[amount][coins]

print num_ways(200, 7)
