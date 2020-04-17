# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 21:25:40 2020

@author: Marek
"""

def Fibonacci():
    
    while True:
    
        try:
            seq_len = int(input('Enter sequence length:\n'))
            break
        except:
            print('Wrong input! Try again')
        
    fib = [0, 1]
    
    for n in range(2, seq_len):
        fib.append(fib[n - 2] + fib[n - 1])
    print(fib)

Fibonacci()    