#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(a):
    '''vector_lengths takes a 2D array of vectors and returns an array of the lengths of the vectors'''
    x = np.sum(a**2, axis=1)
    y = np.sqrt(x)
    return y

def main():
    print(vector_lengths(np.array([[1, 2], [3, 4]])))

if __name__ == "__main__":
    main()
