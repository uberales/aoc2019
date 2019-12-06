#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# input

input_data = []
with open('input.txt', 'r') as f:
    lines = f.readlines()
    input_data = [l.strip().split(')') for l in lines]
    
# structures
    
orbits_down = dict(zip([inp[1] for inp in input_data], [inp[0] for inp in input_data]))

# task 1
        
total = 0
all_centers = orbits_down.values()

for center, satellite in orbits_down.items():
    current = 0
    current += satellite not in all_centers    
    next_center = center
    while next_center != 'COM':        
        current += 1
        next_center = orbits_down[next_center]
    
    total += current

print(total)

# task 2

def track(satellite):
    trace = []
    center = orbits_down[satellite]
    while center != 'COM':
        trace.append(center)
        center = orbits_down[center]
    return trace

trace_you = track('YOU')
trace_san = track('SAN')
last_common = 'COM'

while True:
    if trace_you[-1] == trace_san[-1]:
        last_common = trace_san[-1]
        trace_you.pop()
        trace_san.pop()
    else:
        break
    
print(len(trace_you) + len(trace_san))