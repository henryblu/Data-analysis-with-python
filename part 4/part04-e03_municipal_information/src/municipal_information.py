#!/usr/bin/env python3

import pandas as pd

def main():
    '''reads the file municipal.tsv and prints the shape of the DataFrame and the column names in the following format "col1, col2, col3, ...".'''
    x = pd.read_csv("src/municipal.tsv", sep="\t")
    #x = pd.read_csv("municipal.tsv", sep="\t")
    print(f"Shape: {x.shape[0]},{x.shape[1]}")
    print("Columns:")
    for i in range(len(x.columns)):
        print(x.columns[i])
     


if __name__ == "__main__":
    main()
