#!/usr/bin/env python

def helper():
    for c in range(1, 1000):
        for a in range(1, c):
            b = 1000 - a - c
            if a >= b:
                break
            if a*a + b*b == c*c:
                return a*b*c

print helper()
