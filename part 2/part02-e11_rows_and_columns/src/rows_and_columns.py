#!/usr/bin/env python3

import numpy as np

def get_rows(a):
    '''This function takes a 2D array and returns a list of rows.'''
    rows = []
    for row in a:
        rows.append(row)
    return rows

def get_columns(a):
    '''This function takes a 2D array and returns a list of columns.'''
    columns = []
    for column in a.T:
        columns.append(column)
    return columns

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))

if __name__ == "__main__":
    main()
