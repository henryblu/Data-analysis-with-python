#!/usr/bin/env python3

import numpy as np
import scipy.linalg

def vector_angles(x, y):
    '''vector_angles takes two 2D arrays of vectors and returns an array of the angles between the vectors'''
    x_inner_product = np.sqrt(np.sum(x**2, axis=1))
    y_inner_product = np.sqrt(np.sum(y**2, axis=1))
    x_dot_y = np.sum(x*y, axis=1)
    q = np.clip(x_dot_y/(x_inner_product*y_inner_product), -1, 1)
    alpha = np.arccos(q)
    alpha = np.degrees(alpha)
    return alpha


def main():
    print(vector_angles(np.array([[0, 0, 1], [-1, 1, 0]]), np.array([[0, 0, 1], [-1, 1, 0]])))

if __name__ == "__main__":
    main()
