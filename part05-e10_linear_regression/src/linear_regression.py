#!/usr/bin/env python3

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def fit_line(x, y):
    ''' gets one dimensional arrays x and y as parameters. The function should return the tuple (slope, intercept) of the fitted line. '''
    model = LinearRegression(fit_intercept=True)
    model.fit(x[:, np.newaxis], y)
    return model.coef_[0], model.intercept_
    
def main():
    x = np.array([0, 1, 2, 3, 4, 5])
    y = np.array([1, 3, 2, 5, 7, 8])
    slope, intercept = fit_line(x, y)
    print("Slope: ", slope)
    print("Intercept: ", intercept)
    plt.scatter(x, y)
    plt.plot(x, slope*x + intercept)
    plt.show()
    
if __name__ == "__main__":
    main()
