#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def subfigures(a):
    ''' input a is a 2 dimensional array. this function creates a figure that has 2 subfigures. the first subfigure is a line graph with x coordinates from the first column of a and the y coordinates are in the second column of a. The second subfigure is a scatter plot with x coordinates from the first column of a and the y coordinates are in the second column of a. Additionally, the points should get their color from the third column of a, and size of the point from the fourth column of a. For this, use the c and s named parameters of scatter, respectively'''
    
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot(a[:,0], a[:,1])
    ax2.scatter(a[:,0], a[:,1], c=a[:,2], s=a[:,3])
    plt.show()
    

def main():
    n = 10
    a = np.random.randint(0, 10, (n, 3))
    a = np.concatenate([np.arange(n)[:, np.newaxis], a], axis=1)
    print(a)
    subfigures(a)

if __name__ == "__main__":
    main()
