#!/usr/bin/env python3

import pandas as pd

def growing_municipalities(df):
    '''Returns the percentage of municipalities with growing population'''
    df1 = df[df['Population change from the previous year, %'] > 0]
    return len(df1) / len(df)
    

def main():
    df = pd.read_csv("src/municipal.tsv", sep="\t", index_col=0)
    df = df['Akaa':'Äänekoski']
    growing = growing_municipalities(df)
    print(f"Proportion of growing municipalities: {100*growing:.1f}%")
    return

if __name__ == "__main__":
    main()
