#!/usr/bin/env python

monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

c = 0
#weekday: 0 for Sunday, 1 for Monday, ...
weekday = 1
for y in range(1900, 2001):
    if y%4 == 0 and not (y%100 == 0 and y%400 != 0):
        monthDays[1] = 29
    else:
        monthDays[1] = 28
    for m in monthDays:
        weekday = (weekday + m)%7
        if y > 1900 and weekday == 0:
            c += 1

print c
