#!/usr/bin/env python3

import pandas as pd

def inverse_series(s):
    '''this function takes in a series and returns the series with the values and indexes swapped'''
    return pd.Series(s.index, index=s.values, dtype="object")

def main():
    inverse_series(pd.Series([1,2,3], index=['a', 'b', 'c']))

if __name__ == "__main__":
    main()
