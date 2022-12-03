#!/usr/bin/env python3

import numpy as np

def diamond(n):
    '''This function takes an integer n and returns a diamond of n rows. Do this using the eye and concatenate functions of NumPy and array slicing.'''
    a = np.eye(n, dtype=int)
    b = np.eye(n, dtype=int)[::-1]
    right = np.concatenate((a,b[1:]))
    left = np.concatenate((a,b[1:]))[:,::-1][:,:-1]
    return np.concatenate((left,right), axis=1)


def main():
    print(diamond(3))
    print(diamond(5))

if __name__ == "__main__":
    main()
