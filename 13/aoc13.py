#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from intcode import IntcodeComputer
import copy

opcodes = {}

with open('input.txt', mode='r') as f:
    data = f.read()
    data = [int(i) for i in data.strip().replace('\n',',').split(',')]
    
    opcodes = dict(zip([i for i in range(len(data))], [c for c in data]))

# first
oc_backup = copy.deepcopy(opcodes)
computer = IntcodeComputer(opcodes)

try:
    computer.run()
except IntcodeComputer.IntcodeComputerStatus as e:
    print(e)

def format_output(comp_out):    
    grid_def = [(computer.out_val[3*i], 
                 computer.out_val[3*i+1], 
                 computer.out_val[3*i+2]) for i in range(int(len(computer.out_val)/3))]
    return grid_def

grid_def = format_output(computer.out_val)
print(sum([1 for gd in grid_def if gd[2] == 2]))
pt_str = (' ', '█', '▒', '¯', 'O')

def print_grid(grid_def):
    n_x, n_y = max([pt[0] for pt in grid_def]), max([pt[1] for pt in grid_def])
    grid = [[" " for x in range(n_x+1)] for y in range(n_y+1)]
    
    score = 0
    for pt in grid_def:
        if pt[0] >= 0 and pt[1] >= 0:
            grid[pt[1]][pt[0]] = pt_str[pt[2]]
        else:
            score = pt[2]
    
    for row in grid:
        row_str = ''
        for pt in row:
            row_str += pt
        print(row_str)
    print(score)

opcodes = copy.deepcopy(opcodes)
opcodes[0] = 2
computer = IntcodeComputer(opcodes)

try:
    computer.run()
except IntcodeComputer.IntcodeComputerStatus:
    print_grid(format_output(computer.out_val))
except IntcodeComputer.AwaitsInput:
    print_grid(format_output(computer.out_val))
    in_val = input('Move')