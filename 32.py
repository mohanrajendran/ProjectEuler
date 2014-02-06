# Problem 32
# Pandigital products
#

products = []

def is_pandigital(a,b,c):
    A = str(a)
    B = str(b)
    C = str(c)
    comb = A + B + C

    if len(comb) != 9:
        return False

    for i in range(1,10):
        if str(i) not in comb:
            return False

    return True

for i in range(1, 100):
    if i < 10:
        for j in range(1000, 10000):
            prod = i * j
            if prod not in products and is_pandigital(i,j,prod):
                products.append(prod)
    
    else:
        for j in range(100, 1000):
            prod = i * j
            if prod not in products and is_pandigital(i,j,prod):
                products.append(prod)

print sum(products)
