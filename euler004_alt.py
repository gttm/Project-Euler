#!/usr/bin/env python

def revStr(s):
    rev = ""
    for c in s:
        rev = c + rev
    return rev

def isPalindrome(s):
    l = len(s)
    s1 = s[:l//2]
    s2 = revStr(s)[:l//2]
    return s1 == s2

maxPalindrome = 0
for n1 in range(100, 1000):
    for n2 in range(100, 1000):
        p = n1*n2
        if isPalindrome(str(p)) and p > maxPalindrome:
            maxPalindrome = p

print maxPalindrome
