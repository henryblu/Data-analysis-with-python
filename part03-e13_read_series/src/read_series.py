#!/usr/bin/env python3
import pandas as pd

def read_series():
    '''Reads a series of numbers from the user and returns a series of those numbers. Each line should contain first the index (a-z) and then the corresponding value, separated by whitespace.'''
    data = []
    indexes = []
    while True:
        line = input()
        if line == "":
            break
        try:
            index, value = line.split()
            data.append(value)
            indexes.append(index)
        except:
            print("Malformed input!")
    return pd.Series(data, index=indexes, dtype="object")


    

def main():
    print(read_series())

if __name__ == "__main__":
    main()
