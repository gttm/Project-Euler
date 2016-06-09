#!/usr/bin/env python

sumSq = 0
sqSum = 0
for i in range(1, 101):
    sumSq += i**2
    sqSum += i
sqSum *= sqSum

print sqSum - sumSq
