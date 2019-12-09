#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from intcode import IntcodeComputer

opcodes = {}

with open('input.txt', mode='r') as f:
    data = f.read()
    data = [int(i) for i in data.strip().replace('\n',',').split(',')]
    
    opcodes = dict(zip([i for i in range(len(data))], [c for c in data]))

# first

computer = IntcodeComputer(opcodes)

try:
    computer.run(in_val = 1)
except IntcodeComputer.IntcodeComputerStatus as e:
    print(e)
    
print(computer.out_val)

# second

computer.reset(opcodes)

try:
    computer.run(in_val = 2)
except IntcodeComputer.IntcodeComputerStatus as e:
    print(e)
    
print(computer.out_val)
