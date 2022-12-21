#!/usr/bin/env python3

import pandas as pd

def subsetting_with_loc():
    '''this function reads the municipal data and returns the population and percent of swedish speakers and foreign citizens'''
    df = pd.read_csv("src/municipal.tsv", sep="\t", index_col=0)
    df = pd.DataFrame(df.loc['Akaa':'Äänekoski', ['Population', 'Share of Swedish-speakers of the population, %', "Share of foreign citizens of the population, %"]])
    return df

def main():
    subsetting_with_loc()
    return

if __name__ == "__main__":
    main()
