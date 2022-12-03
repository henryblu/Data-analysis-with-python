#!/usr/bin/env python3

import numpy as np

def column_comparison(a):
    '''takes in a 2d array, returns a 2d array which have a larger value in their 2nd coulmn than their 2nd last column'''
    return a[a[:,1]>a[:,-2]]
    
def main():
    pass

if __name__ == "__main__":
    main()
