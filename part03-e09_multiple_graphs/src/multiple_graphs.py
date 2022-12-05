#!/usr/bin/env python3

import matplotlib.pyplot as plt

def main():
    ''' This function plot the following two graphs in one axes. The first graphs has x coordinates 2,4,6,7 and y coordinates 4,3,5,1. The second graph has x coordinates 1,2,3,4 and y coordinates 4,2,3,1.'''
    x1 = [2,4,6,7]
    y1 = [4,3,5,1]
    x2 = [1,2,3,4]
    y2 = [4,2,3,1]
    plt.plot(x1, y1, x2, y2)
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title('title')
    plt.show()



if __name__ == "__main__":
    main()
