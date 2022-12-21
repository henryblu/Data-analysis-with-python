#!/usr/bin/env python3

import pandas as pd

def create_series(L1, L2):
    ''' input is two lists of numbers with length 3. the function turns these lists into seriese with index a, b, c and returns the two series'''
    s1 = pd.Series(L1, index=['a', 'b', 'c'])
    s2 = pd.Series(L2, index=['a', 'b', 'c'])
    return (s1, s2)
    
def modify_series(s1, s2):
    ''' input is two series of length 3. the function moves the the second value from series s2 to s1 and returns the two series'''
    s1['d'] = s2['b']
    s2 = s2.drop('b')
    return (s1, s2)
    
def main():
    s1,s2=create_series([1,2,3], [4,5,6])
    s1,s2=modify_series(s1, s2)
    print(s1+s2)
    
if __name__ == "__main__":
    main()
