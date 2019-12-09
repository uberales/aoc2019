#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class IntcodeComputer():

    from enum import IntEnum
    
    class IntcodeComputerStatus(Exception):
        pass
    
    class AwaitsInput(IntcodeComputerStatus):
        pass
    
    class ComputationDone(IntcodeComputerStatus):
        pass
    
    class Modes(IntEnum):
        POSITION = 0
        IMMEDIATE = 1
        RELATIVE = 2

    stack = {}
    relative_base = 0
    out_val = []
    in_val = []
    state_i = 0
        
    def __init__(self, stack):
        import copy
        self.stack = copy.deepcopy(stack)
  
    def stack_read(self, address):
        return 0 if address not in self.stack else self.stack[address]  

    def stack_write(self, address, val):
        if address < 0:
            raise KeyError('Illegal memory address')
        self.stack[address] = val

    def resolve_value(self, i, mode):        
        if mode == self.Modes.POSITION: # position mode
            return self.stack_read(self.stack_read(i))
        elif mode == self.Modes.IMMEDIATE: # immediate mode
            return self.stack_read(i)
        elif mode == self.Modes.RELATIVE: # relative mode
            return self.stack_read(self.relative_base + self.stack_read(i))
        else:
            raise NotImplementedError

    def resolve_address(self, i, mode):
        if mode == self.Modes.POSITION: # position mode
            return self.stack_read(i)
        elif mode == self.Modes.IMMEDIATE: # immediate mode
            raise ValueError('Invalid reading mode')
        elif mode == self.Modes.RELATIVE: # relative mode
            return self.relative_base + self.stack_read(i)
        else:
            raise NotImplementedError

    def opcode(self, oc_i):
        oc = self.stack_read(oc_i)
                       
        oc_def = oc % 100
        mode_1 = int((oc % 1000) / 100)
        mode_2 = int((oc % 10000) / 1000)
        mode_3 = int((oc % 100000) / 10000)        
        
        if oc_def == 1:
            val_1 = self.resolve_value(oc_i + 1, mode_1)
            val_2 = self.resolve_value(oc_i + 2, mode_2)
            address = self.resolve_address(oc_i + 3, mode_3)
            self.stack_write(address, val_1 + val_2)
            next_i = oc_i + 4
        elif oc_def == 2:
            val_1 = self.resolve_value(oc_i + 1, mode_1)
            val_2 = self.resolve_value(oc_i + 2, mode_2)
            address = self.resolve_address(oc_i + 3, mode_3)
            self.stack_write(address, val_1 * val_2)
            next_i = oc_i + 4
        elif oc_def == 3:
            val = None
            if type(self.in_val) is int:
                val = self.in_val
                self.in_val = None
            elif type(self.in_val) is list and len(self.in_val) > 0:
                val = self.in_val.pop(0)    
                
            if val is None:
                raise self.AwaitsInput('Waiting for input')
            else:
                address = self.resolve_address(oc_i + 1, mode_1)
                self.stack_write(address, val)
                next_i = oc_i + 2
        elif oc_def == 4:
            val_1 = self.resolve_value(oc_i + 1, mode_1)
            self.out_val.append(val_1)
            next_i = oc_i + 2
        elif oc_def == 5:
            val_1 = self.resolve_value(oc_i + 1, mode_1)
            val_2 = self.resolve_value(oc_i + 2, mode_2)
            if val_1 != 0:
                next_i = val_2
            else:
                next_i = oc_i + 3
        elif oc_def == 6:
            val_1 = self.resolve_value(oc_i + 1, mode_1)
            val_2 = self.resolve_value(oc_i + 2, mode_2)
            if val_1 == 0:
                next_i = val_2
            else:
                next_i = oc_i + 3
        elif oc_def == 7:
            val_1 = self.resolve_value(oc_i + 1, mode_1)
            val_2 = self.resolve_value(oc_i + 2, mode_2)
            address = self.resolve_address(oc_i + 3, mode_3)
            self.stack_write(address, 1 if val_1 < val_2 else 0)
            next_i = oc_i + 4
        elif oc_def == 8:
            val_1 = self.resolve_value(oc_i + 1, mode_1)
            val_2 = self.resolve_value(oc_i + 2, mode_2)
            address = self.resolve_address(oc_i + 3, mode_3)
            self.stack_write(address, 1 if val_1 == val_2 else 0)

            next_i = oc_i + 4
        elif oc_def == 9:
            val_1 = self.resolve_value(oc_i + 1, mode_1)
            self.relative_base += val_1
            next_i = oc_i + 2
        elif oc_def == 99:
            raise self.ComputationDone('Done')
        return next_i
    
    def run(self, in_val = None, reset_output = False):
        self.in_val = in_val
        
        if reset_output:
            self.out_val = []
        
        next_i = self.state_i
        while True:                 
            self.state_i = next_i        
            next_i = self.opcode(next_i)        

    def reset(self, stack):
        import copy
        self.stack = copy.deepcopy(stack)
        self.relative_base = 0
        self.out_val = []
        self.in_val = []
        self.state_i = 0
