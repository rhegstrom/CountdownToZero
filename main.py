# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 18:04:53 2022

@author: Roger Hegstrom

Write a Python module that computes the number of steps required for the sequence to get 'down to 1.'

Given any positive integer, n at each step do this:
   - If n is odd,  replace n with 3*n+1
   - If n is even, replace n with n/2

for example if n =11 the the sequence is  11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1
it took 14 steps

print out the number of steps required for the integers 5 through 20
"""


def compute(n):
    seq = [n,]
    
    while n != 1:
        if n % 2:
            # Odd
            n = 3 * n + 1 
        else:
            # Even
            n = int(n / 2)
            
        seq.append(n)
    
    return seq


# Print out the number of steps required for the integers 5 through 20
for i in range(5, 21):
    seq = compute(i)
    
    print(f'i={i:2}, steps={len(seq)-1:2}, {seq}')




    
            
            