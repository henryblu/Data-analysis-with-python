#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a):
    '''gets a two dimensional array of shape (n,2*m) as a parameter. the function returns all rows with a larger first half sum than the second half sum'''
    left_sum = np.sum(a[:,:a.shape[1]//2], axis=1)
    right_sum = np.sum(a[:,a.shape[1]//2:], axis=1)
    return a[left_sum>right_sum]


def main():
    a = np.array([[1, 3, 4, 2],
                [2, 2, 1, 2]])
    print(first_half_second_half(a))

if __name__ == "__main__":
    main()
