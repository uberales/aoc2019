#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy

opcodes = []

with open('input.txt', mode='r') as f:
    data = f.read()
    opcodes = [int(i) for i in data.strip().replace('\n',',').split(',')]

def intcode_comp(stack, in_val = None, init_i = 0):
    out_val = None
    
    def par_val(par_i, par_mode):
        return stack[stack[par_i]] if par_mode == 0 else stack[par_i]
        
    def opcode(oc_i, stack):
        nonlocal in_val
        out_val = None
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
            val = None
            if type(in_val) is int:
                val = in_val
                in_val = None
            elif type(in_val) is list and len(in_val) > 0:
                val = in_val.pop(0)      
            if val is None:
                next_i = -3
            else:
                stack[stack[oc_i + 1]] = val
                next_i = oc_i + 2
        elif oc_def == 4:
            val = int(stack[stack[oc_i + 1]])
            out_val = val
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
        return next_i, out_val

    next_i = init_i
    state_i = init_i
    while next_i >= 0:
        state_i = next_i
        next_i, ov = opcode(next_i, stack)
        out_val = ov if ov is not None else out_val
    
    return out_val, next_i, state_i

# first

def amplifier(phase_setting):
    out_val = 0
    amp_opcodes = [copy.deepcopy(opcodes) for i in range(5)] # fortunately, there are no modifiers
    while True:
        for i in range(5):
            out_val, next_i, *_ = intcode_comp(amp_opcodes[i], in_val = [phase_setting[i], out_val])
        
        if next_i == -1:
            break
    return out_val

out_max = 0

def eval_max(phase_setting):
    global out_max
    out_max = max(out_max, amplifier(phase_setting))

def permute(seq_0, i_from, process_fn, depth = 0):    
    
    for i in range(i_from, len(seq_0)):
        seq = copy.deepcopy(seq_0)
        seq[i_from], seq[i] = seq[i], seq[i_from]

        if i_from < len(seq):
            permute(seq, i_from + 1, process_fn, depth = depth + 1)
            
    if i_from == len(seq_0):
        process_fn(seq_0)

permute([0, 1, 2, 3, 4], 0, eval_max)

print(out_max)

out_max_fb = 0

# second

def eval_max_feedback(phase_setting):
    global out_max_fb
    out_max_fb = max(out_max, amplifier_feedback(phase_setting))
    
def amplifier_feedback(phase_setting):
    
    amp_opcodes = [copy.deepcopy(opcodes) for i in range(5)]
    amp_states = [0 for i in range(5)]
       
    for i in range(5):
        out_val, next_i, amp_states[i] = intcode_comp(amp_opcodes[i], in_val = phase_setting[i])
            
    out_val = 0
    
    while True:
        for i in range(5):
            out_val, next_i, amp_states[i] = intcode_comp(amp_opcodes[i], in_val = out_val, init_i = amp_states[i])       
        if next_i == -1:
            break

    return out_val

permute([5, 6, 7, 8, 9], 0, eval_max_feedback)

print(out_max)