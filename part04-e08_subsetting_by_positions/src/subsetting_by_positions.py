#!/usr/bin/env python3

import pandas as pd

def subsetting_by_positions():
    ''' reads the UK-top40 and Returns the top 10 entries and only the columns Title and Artist'''
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    df = pd.DataFrame(df.iloc[0:10, [2, 3]])

    return df

def main():
    subsetting_by_positions()
    return

if __name__ == "__main__":
    main()
