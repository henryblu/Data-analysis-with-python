#!/usr/bin/env python3

import scipy.stats
import numpy as np

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

def lengths():
    '''retruns the pearson correlation coefficients between petal length and sepal length of the iris data set'''
    stat,pval = scipy.stats.pearsonr(x = load()[:,0], y= load()[:,2])
    return stat

def correlations():
    '''returns a 2d array of the Pearson correlation coefficients between the columns of the iris data set'''
    return np.corrcoef(load(), rowvar=False)

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
