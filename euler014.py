#!/usr/bin/env python

def sequenceLen(n, sequences):
    if n in sequences:
        return sequences[n]
    elif n%2 == 0:
        res = sequenceLen(n/2, sequences) + 1
        sequences[n] = res
        return res
    else:
        res = sequenceLen(3*n + 1, sequences) + 1
        sequences[n] = res
        return res

maxLen = 0
res = 0
sequences = {1: 1}
for i in range(1, 1000000):
    l = sequenceLen(i, sequences)
    if l > maxLen:
        maxLen = l
        res = i

print res
