#!/usr/bin/env python

def calcMaxTotal(i, j, triangle, maxTotals):
    if maxTotals[i][j] == 0:
        maxTotals[i][j] = max(calcMaxTotal(i + 1, j, triangle, maxTotals), 
                              calcMaxTotal(i + 1, j + 1, triangle, maxTotals)) + triangle[i][j]
    return maxTotals[i][j]

f = open("p067_triangle.txt", "r")

triangle = [[int(n) for n in l.split()] for l in f]

maxTotals = [[0 for j in range(0, i)] for i in range(1, len(triangle))]
maxTotals += [triangle[-1]]

print calcMaxTotal(0, 0, triangle, maxTotals)
