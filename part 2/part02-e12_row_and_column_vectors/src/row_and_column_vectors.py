#!/usr/bin/env python3

import numpy as np

def get_row_vectors(a):
    '''This function takes a 2D array (n,m) and returns a list of rows in the shape (1,m)'''
    rows = []
    for row in a:
        rows.append(np.array([row]))

    return rows

def get_column_vectors(a):
    '''This function takes a 2D array (n,m) and returns a list of columns in the shape (n,1)'''
    columns = []
    for column in a.T:
        columns.append(np.array([column]).T)
    return columns

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Row vectors:", get_row_vectors(a))
    print("Column vectors:", get_column_vectors(a))

if __name__ == "__main__":
    main()
