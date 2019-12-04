#!/usr/bin/env python3
# -*- coding: utf-8 -*-

i_from = 158126
i_to = 624574

def has_double(digits):
    for i in range(len(digits) - 1):
        if digits[i] == digits[i + 1]:
            return True
    return False

def has_proper_double(digits):
    i = 0
    n = len(digits)
    while i < n:
        count = 1
        d = digits[i]
        while i < n - 1:
            if digits[i + 1] == d:
                count += 1
                i += 1
            else:
                break
        if count == 2:
            return True
        i += 1
    return False

def is_ascending(digits):
    for i in range(len(digits) - 1):
        if digits[i] > digits[i + 1]:
            return False
    return True

# part 1

count = 0

for pw in range(i_from, i_to + 1):
    digits = [int(d) for d in str(pw)]
    count += int(has_double(digits) and is_ascending(digits))

print(count)

# part 2

count = 0

for pw in range(i_from, i_to + 1):
    digits = [int(d) for d in str(pw)]
    count += int(has_proper_double(digits) and is_ascending(digits))

print(count)