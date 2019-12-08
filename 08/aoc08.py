#!/usr/bin/env python3
# -*- coding: utf-8 -*-

w = 25
h = 6
    
def layers(): 
    with open('input.txt', mode='r') as f:        
        while True:
            data = f.read(w * h)
            if not data:
                break
            yield data.strip()

# part 1

min_zeros = None
result = 0

for layer in layers():
    if len(layer) > 0:            
        zeros = layer.count('0')        
        if min_zeros is None or zeros < min_zeros:
            min_zeros = zeros
            result = layer.count('1') * layer.count('2')

print(result)

# part 2

image = [2 for i in range(w * h)]

for layer in layers():
    if len(layer) > 0:
        for i in range(w * h):
            if int(layer[i]) < 2 and image[i] == 2:
                image[i] = int(layer[i])

for r in range(h):
    line = ''
    for c in range(w):
        i = c + r * w
        line += 'O' if image[i] == 1 else ' '
    print(line)

    