#!/usr/bin/env python

primes = [2]
i = 3
c = 1
while c < 10001:
    isPrime = True
    for j in primes:
        if j*j > i:
            break
        if i%j == 0:
            isPrime = False
            break
    if isPrime:
        primes.append(i)
        c += 1
    i += 1

print primes[-1]
