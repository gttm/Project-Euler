#!/usr/bin/env python

def helper(palindromes):
    for p in palindromes:
        for i in range (100, 1000):
            if  p%i == 0 and p//i > 99 and p//i < 1000:
                return p

palindromes = []
for n in range(999, 99, -1):
    palindromes.append(int(str(n) + str(n)[::-1]))

print helper(palindromes)
