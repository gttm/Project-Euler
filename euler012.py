#!/usr/bin/env python

triangle = 0
i = 1
while 1:
    triangle += i
    i += 1
    divisors = 1
    j = 2
    while j*j <= triangle:
        if triangle%j == 0:
            divisors += 1
        j += 1
#divisors under the root of the number are equal to the divisors over the root
    divisors *= 2
    if divisors > 500:
        print triangle
        break
