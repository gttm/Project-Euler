#!/usr/bin/env python

primes = [2]
for i in range(3, 2000000):
    isPrime = True
    for j in primes:
        if j*j > i:
            break
        if i%j == 0:
            isPrime = False
            break
    if isPrime:
        primes.append(i)

print sum(primes)
