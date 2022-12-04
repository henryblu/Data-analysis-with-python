#!/usr/bin/env python3
import numpy as np
import functools

def matrix_power(a, n):
    '''inputs are a square matrix 'a' and an integer 'n'. TThe function returns the matrix a multiplied by itself n-1 times. done using reduce function and generator function'''
    neg = False

    if n < 0:
        neg = True
        n = abs(n)
    
    if n == 0:
        return np.eye(a.shape[0])
        
    elif n != 1:
        a = functools.reduce(lambda x, y: x @ y, (a for i in range(n)))
    
    if neg == True:
        return np.linalg.inv(a)
    return a
    

def main():
    print(np.linalg.matrix_power(np.array([[1, 2], [3, 4]]), -3))
    print(matrix_power(np.array([[1, 2], [3, 4]]), -3))

if __name__ == "__main__":
    main()


