#!/usr/bin/env python3

import numpy as np

def most_frequent_first(a, c):
    '''takes in a 2d array and a coulmn index c. returns a 2d array where the rows are sorted by the frequency of the value in the column c'''
    uniques, counts = np.unique(a[:,c], return_counts=True)
    # zip the two arrays together, sort by the counts, then unzip
    uniques, counts = zip(*sorted(zip(uniques, counts), key=lambda x: x[1], reverse=True))
    uniques = np.array(uniques)
    


    

def main():
    a = np.array([[2, 4, 1, 2],
                [1, 3, 4, 2],
                [2, 2, 1, 2], 
                [1, 3, 4, 2],
                [2, 2, 1, 2],
                [1, 3, 4, 2],
                [2, 4, 1, 2],
                [2, 4, 1, 2]])
    print(most_frequent_first(a, 1))

if __name__ == "__main__":
    main()
