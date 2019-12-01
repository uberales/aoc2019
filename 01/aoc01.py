#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 11:18:39 2019

@author: ales
"""

import numpy as np

modules = []

with open('input.txt', mode='r') as f:
    data = f.readlines()
    modules = [int(d.strip()) for d in data]

def fuel(mass):
    fuel = np.floor(mass / 3) - 2
    return fuel

total_fuel = sum([fuel(m) for m in modules])

print(total_fuel)

def extra_fuel(mass):
    add_fuel = fuel(mass)
    extra_fuel = add_fuel
    
    while True:
        add_fuel = fuel(add_fuel)
        if add_fuel <= 0:
            break
            
        extra_fuel += add_fuel

    return extra_fuel

total_fuel_adjusted = sum([extra_fuel(m) for m in modules])

print(total_fuel_adjusted)