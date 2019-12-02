#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy

opcodes = []

with open('input.txt', mode='r') as f:
    data = f.read()
    opcodes = [int(i) for i in data.strip().replace('\n',',').split(',')]

def intcode_comp(stack):
    def opcode(oc_i, stack):
        oc = stack[oc_i]
        next_i = -2
        if oc == 1:
            stack[stack[oc_i + 3]] = stack[stack[oc_i + 1]] + stack[stack[oc_i + 2]]
            next_i = oc_i + 4
        elif oc == 2:
            stack[stack[oc_i + 3]] = stack[stack[oc_i + 1]] * stack[stack[oc_i + 2]]
            next_i = oc_i + 4
        elif oc == 99:
            next_i = -1
        return next_i

    next_i = 0
    while next_i >= 0:
        next_i = opcode(next_i, stack)
    return stack[0]

# first
opcodes_mod = copy.deepcopy(opcodes)

opcodes_mod[1] = 12
opcodes_mod[2] = 2

print(intcode_comp(opcodes_mod))

# second
desired = 19690720

for noun in range(100):
    do_break = False
    for verb in range(100):
        opcodes_mod = copy.deepcopy(opcodes)
        opcodes_mod[1] = noun
        opcodes_mod[2] = verb
        result = intcode_comp(opcodes_mod)
        if result == desired:
            do_break = True
            print(100 * noun + verb)
            break
    if do_break:
        break
    