#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy

opcodes = []

with open('input.txt', mode='r') as f:
    data = f.read()
    opcodes = [int(i) for i in data.strip().replace('\n',',').split(',')]

def intcode_comp(stack):
    def par_val(par_i, par_mode):
        return stack[stack[par_i]] if par_mode == 0 else stack[par_i]
        
    def opcode(oc_i, stack):
        oc = stack[oc_i]
        
        oc_parts = [c for c in str(oc)]
        oc_def = int('{}{}'.format(oc_parts[-2], oc_parts[-1])) if len(oc_parts) > 1 else int(oc_parts[-1])
        mode_1 = int(oc_parts[-3]) if len(oc_parts) > 2 else 0
        mode_2 = int(oc_parts[-4]) if len(oc_parts) > 3 else 0
        mode_3 = int(oc_parts[-5]) if len(oc_parts) > 4 else 0
        
        next_i = -2
        if oc_def == 1:
            val_1 = par_val(oc_i + 1, mode_1)
            val_2 = par_val(oc_i + 2, mode_2)
            stack[stack[oc_i + 3]] = val_1 + val_2
            next_i = oc_i + 4
        elif oc_def == 2:
            val_1 = par_val(oc_i + 1, mode_1)
            val_2 = par_val(oc_i + 2, mode_2)
            stack[stack[oc_i + 3]] = val_1 * val_2
            next_i = oc_i + 4
        elif oc_def == 3:
            val = input('Give me an integer:')
            val = int(val)
            stack[stack[oc_i + 1]] = val
            next_i = oc_i + 2
        elif oc_def == 4:
            val = int(stack[stack[oc_i + 1]])
            print('The output is:', val)
            next_i = oc_i + 2
        elif oc_def == 5:
            val_1 = par_val(oc_i + 1, mode_1)
            val_2 = par_val(oc_i + 2, mode_2)
            if val_1 != 0:
                next_i = val_2
            else:
                next_i = oc_i + 3
        elif oc_def == 6:
            val_1 = par_val(oc_i + 1, mode_1)
            val_2 = par_val(oc_i + 2, mode_2)
            if val_1 == 0:
                next_i = val_2
            else:
                next_i = oc_i + 3
        elif oc_def == 7:
            val_1 = par_val(oc_i + 1, mode_1)
            val_2 = par_val(oc_i + 2, mode_2)
            if val_1 < val_2:
                stack[stack[oc_i + 3]] = 1
            else:
                stack[stack[oc_i + 3]] = 0
            next_i = oc_i + 4
        elif oc_def == 8:
            val_1 = par_val(oc_i + 1, mode_1)
            val_2 = par_val(oc_i + 2, mode_2)
            if val_1 == val_2:
                stack[stack[oc_i + 3]] = 1
            else:
                stack[stack[oc_i + 3]] = 0
            next_i = oc_i + 4
        elif oc_def == 99:
            next_i = -1
        return next_i

    next_i = 0
    while next_i >= 0:
        next_i = opcode(next_i, stack)
    return stack[0]

# first
opcodes_mod = copy.deepcopy(opcodes)

intcode_comp(opcodes_mod)
