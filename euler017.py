#!/usr/bin/env python

words_key = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    1000: 'onethousand'
}

words = {}

for i in range(1, 1001):
    if i in words_key:
        words[i] = words_key[i]
        continue
    words[i] = ''
    if i >= 100:
        words[i] += words_key[i//100] + 'hundred'
        if i%100 == 0:
            continue
        words[i] += 'and'
    d = i%100
    if d in words_key:
        words[i] += words_key[d]
        continue
    words[i] += words_key[d//10*10] + words_key[d%10]

print sum([len(w) for n, w in words.iteritems()])
