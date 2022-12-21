#!/usr/bin/env python3

import pandas as pd

def powers_of_series(s, k):
    '''takes in a series s, and a integer k, and returns a dataframe which has the powers of the series s from 1 to k as columns.'''
    df = pd.DataFrame()
    for i in range(1, k+1):
        df[i] = s ** i
    return df
    
def main():
    s = pd.Series([1,2,3,4], index=list("abcd"))
    print(s)  
    print(powers_of_series(s, 3))  
    
if __name__ == "__main__":
    main()
