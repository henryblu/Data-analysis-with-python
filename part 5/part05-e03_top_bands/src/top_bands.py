#!/usr/bin/env python3

import pandas as pd

def top_bands():
    '''Reads the data from the file bands.tsv and UK-top40-1964-1-2.tsv and returns a merged dataframe'''
    df1 = pd.read_csv('src/bands.tsv', sep='\t')
    df2 = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')
    df1["Band"] = df1["Band"].str.upper()
    df = pd.merge(df1, df2, left_on='Band', right_on='Artist')
    return df
    
def main():
    df = top_bands()
    print("Shape:", df.shape)
    print("Column names:\n", df.columns)
    print(df.head())

if __name__ == "__main__":
    main()
