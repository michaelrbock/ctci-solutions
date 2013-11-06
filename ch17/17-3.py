import math

def trailing_zeros_in_factorial(n):
    fact = str(math.factorial(n))
    zeros = 0
    for i in xrange(len(fact)-1, -1, -1):
        if fact[i] != "0":
            break
        zeros += 1
    return zeros
