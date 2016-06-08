#!/usr/bin/env python
import math

def getLargestPrimeFactor(n):
    i = int(math.floor(math.sqrt(n)))
    maxPrime = 0
    while i >= 2:
        if n % i == 0:
            res = getLargestPrimeFactor(i)
            if maxPrime < res:
                maxPrime = res
        i -= 1
    if maxPrime == 0:
        maxPrime = n
    return maxPrime

print getLargestPrimeFactor(600851475143)
