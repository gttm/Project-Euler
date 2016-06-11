#!/usr/bin/env python
import math

def d(n):
    c = 1
    sqrt = int(math.sqrt(n))
    for i in range(2, sqrt + 1):
        if n%i == 0:
            c += i + n//i
    if n == sqrt*sqrt:
        c -= sqrt
    return c

abundant = [i for i in range(1, 28123) if d(i) > i]
abundantSums = {i + j for i in abundant for j in abundant if i + j <= 28123}

print sum([i for i in range(1, 28124) if i not in abundantSums])
