#!/usr/bin/env python3

import numpy as np

def multiplication_table(n):
    '''creates a multiplication table of size n from 0 to n-1'''
    x = np.arange(n)
    y = np.arange(n)
    x, y = np.meshgrid(x, y)
    return x*y
    

def main():
    print(multiplication_table(4))

if __name__ == "__main__":
    main()
