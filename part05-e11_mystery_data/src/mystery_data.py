#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def mystery_data():
    ''' Read the tab separated file mystery_data.tsv. Its first five columns define the features, and the last column is the response..csv and returns the coefficients of the fitted line.'''
    df = pd.read_csv("src/mystery_data.tsv", sep="\t")
    x = df.iloc[:, :-1]
    y = df.iloc[:, -1]
    model = LinearRegression(fit_intercept=False)
    model.fit(x, y)
    return model.coef_


def main():
    coefficients = mystery_data()
    for i in range(len(coefficients)):
        print(f'Coefficient of X{i+1} is {coefficients[i]}')
    # print the coefficients here
    
if __name__ == "__main__":
    main()
