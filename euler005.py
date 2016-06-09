#!/usr/bin/env python

primes = [2]
for i in range(3, 21):
    isPrime = True
    for j in primes:
        if j*j > i:
            break
        if i%j == 0:
            isPrime = False
            break
    if isPrime:
        primes.append(i)

factors = {}
for i in range(2, 21):
    if i in primes:
        factors[i] = 1
    else:
        for f, c in factors.iteritems():
            if i%(f**(c + 1)) == 0:
                factors[f] = c + 1
    print i, factors

prod = 1
for f, c in factors.iteritems():
    prod *= f**c
print prod
