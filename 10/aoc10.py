#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

field = []

with open('input.txt', mode='r') as f:
    lines = f.readlines()
    field = [list(l.strip()) for l in lines]

visibility = [[0 for asteroid in line] for line in field]

height = len(field)
width = len(field[0])

def check(i, dim):
    return i >= 0 and i < dim

directions = set()
def add_dir(dx, dy):
    multiples = (-1, 1)
    for m1 in multiples:
        for m2 in multiples:
            directions.add((m1 * dx, m2 * dy))
            directions.add((m1 * dy, m2 * dx))

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# preparation

add_dir(0, 1)
for dx in range(1, width + 1):
    for dy in range(1, height + 1):
        if (gcd(dx, dy) == 1 and gcd(dy, dx) == 1):
            add_dir(dx, dy)

# part 1

for y in range(height):
    for x in range(width):
        if field[y][x] == '#':
            for d in directions:
                n = 1
                while check(x + n * d[0], width) and check(y + n * d[1], height):
                    if field[y + n * d[1]][x + n * d[0]] == '#':
                        visibility[y][x] += 1
                        break
                    n += 1

max_visibility = max([max(l) for l in visibility])
print(max_visibility)

# part 2

turret = None
for y in range(height):
    for x in range(width):
        if visibility[y][x] == max_visibility:
            turret = (x, y)
            break
    if turret is not None:
        break

# sort the directions clockwise
directions = sorted(list(directions), key=lambda d: -np.arctan2(d[0], d[1]))

d_i = 0
count = 0
while True:
    d = directions[d_i]
    
    n = 1
    x = turret[0] + n * d[0]
    y = turret[1] + n * d[1]
    
    while check(x, width) and check(y, height):
        if field[y][x] == '#':
            field[y][x] = 'X'
            count += 1
            break
        n += 1
        x = turret[0] + n * d[0]
        y = turret[1] + n * d[1]
        
    if count == 200:
        result = 100 * x + y
        print(result)
        break
    
    d_i = (d_i + 1) % len(directions)
    