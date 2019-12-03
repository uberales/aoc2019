#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

directions = {'L': (-1, 0), 'U': (0, 1), 'R': (1, 0), 'D': (0, -1)}

wire_a = []
wire_b = []

ex = re.compile('([RLDU])([0-9]*)')

with open('input.txt') as f:
    lines = f.readlines()
    wire_a = [(re.match(ex, s.strip()).group(1), int(re.match(ex, s.strip()).group(2))) for s in lines[0].split(',')]
    wire_b = [(re.match(ex, s.strip()).group(1), int(re.match(ex, s.strip()).group(2))) for s in lines[1].split(',')]

def walk(wire):
    path = [(0, 0)] # part 1
    steps = {(0, 0): 0} # part 2
    step = 0
    for seg in wire:
        direction = directions[seg[0]]
        for i in range(seg[1]):
            step += 1
            point = (path[-1][0] + direction[0], path[-1][1] + direction[1])
            path.append(point)
            steps[point] = step
    return path, steps

path_a, steps_a = walk(wire_a)
path_b, steps_b = walk(wire_b)

common_points = set.intersection(set(path_a), set(path_b))

distances = sorted([abs(pt[0]) + abs(pt[1]) for pt in common_points])
print(distances[1])

step_counts = sorted([steps_a[pt] + steps_b[pt] for pt in common_points])
print(step_counts[1])
