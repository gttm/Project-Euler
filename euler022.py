#!/usr/bin/env python

f = open("p022_names.txt", "r")

names = [s.replace('"', '') for s in f.readline().split(',')]
names.sort()

s = 0
for i in range(0, len(names)):
    s += (i + 1)*sum([ord(c) - ord('A') + 1 for c in names[i]])

print s
