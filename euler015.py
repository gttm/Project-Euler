#!/usr/bin/env python

def calcPaths(x, y, paths):
    if x == grid or y == grid:
        paths[x][y] = 1
    if paths[x][y] == 0:
        paths[x][y] = calcPaths(x + 1, y, paths) + calcPaths(x, y + 1, paths)
    return paths[x][y]

grid = 20
paths = [[0 for j in range(grid + 1)] for i in range(grid + 1)]
        
print calcPaths(0, 0, paths)
