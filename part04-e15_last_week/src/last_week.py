#!/usr/bin/env python3

import pandas as pd
import numpy as np

def last_week():
    df = pd.read_csv("UK-top40-1964-1-2.tsv", sep="\t")
    # first we get rid of the new songs and re-entries and replace those rows with nan
    df = df[df['LW'] != 'New']
    df = df[df['LW'] != 'Re']
    df['LW'] = df['LW'].astype(int)

    # now we suybtract 1 from WoC
    df['WoC'] = (df['WoC'] - 1).astype(int)
    # if the peak position is the same as the current position but not the same as last weeks position, then the peak position is replaced with nan
    df.loc[(df['Pos'] == df['Peak Pos']) & (df['LW'] != df['Peak Pos']), 'Peak Pos'] = np.nan

    # Now we replace the current position with last week's position
    df['Pos'] = df['LW']
    # Now we change last weeks postion to nan and then sort by position
    df['LW'] = np.nan
    df = df.sort_values(by=['Pos'])
    
    # now we add back missing 3 postitions 
    new_index = pd.Index(np.arange(1, 41, 1), name='Pos')
    df = df.set_index('Pos').reindex(new_index).reset_index()
    return df

def main():
    df = last_week()
    print(df)
    


if __name__ == "__main__":
    main()
