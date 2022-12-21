#!/usr/bin/env python3

import numpy as np

def most_frequent_first(a, c):
    '''takes in a 2d array and a coulmn index c. function sorts the array by the frequency of the values in column c. returns the sorted array'''
    
    # create frequency dictionary for values in coulmn c
    uc = {}
    uniques, counts = np.unique(a[:,c], return_counts=True)
    for i in range(len(uniques)):
        uc[uniques[i]] = counts[i]

    # make a new dictionary with the rows sorted by frequency of the values in column c
    sorted_array = np.array([])
    for key, value in sorted(uc.items(), key=lambda item: item[1], reverse=True):
        for row in a:
            if row[c] == key:
                sorted_array = np.append(sorted_array, row)
    return sorted_array.reshape(a.shape[0], a.shape[1])

    

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
