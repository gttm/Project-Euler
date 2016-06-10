#!/usr/bin/env python

f1 = 1
f2 = 2
s = 0
while f2 < 4000000:
    if f2%2 == 0:
        s += f2
    tmp = f1 + f2
    f1 = f2
    f2 = tmp
print s
