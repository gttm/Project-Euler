#!/usr/bin/env python

def d(n):
    c = 0
    for i in range(1, n//2 + 1):
        if n%i == 0:
            c += i
    return c

sums = [d(i) for i in range(0, 10000)]

s = 0
for i in range(1, 10000):
    if sums[i] == i or sums[i] >= 10000: 
        continue
    if i == sums[sums[i]]:
        s += i

print s
