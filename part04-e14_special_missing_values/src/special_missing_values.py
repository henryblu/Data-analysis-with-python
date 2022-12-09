#!/usr/bin/env python3

import pandas as pd
import numpy as np

def special_missing_values():
    '''This function reads the data set of the top forty singles from the beginning of the year 1964 from the src folder. It Return the rows whose singles' position dropped compared to last week's position (column LW=Last Week).'''
    df = pd.read_csv('src/UK-top40-1964-1-2.tsv',sep='\t')
    df = df.replace({'Re':np.nan,'New':np.nan})
    df['LW'] = df['LW'].astype(float)
    return df[df['LW'] < df['Pos']]

def main():
    df = special_missing_values()
    print(df)

if __name__ == "__main__":
    main()
