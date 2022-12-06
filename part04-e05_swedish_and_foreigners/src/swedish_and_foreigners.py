#!/usr/bin/env python3

import pandas as pd

def swedish_and_foreigners():
    '''this function reads the municipal data and returns the municipalities that have more than 5% swedish speakers and foreign citizens'''
    df = pd.read_csv("src/municipal.tsv", sep="\t", index_col=0)
    df = df['Akaa':'Äänekoski']
    df = df[df['Share of Swedish-speakers of the population, %'] > 5.0]
    df = df[df['Share of foreign citizens of the population, %'] > 5.0]
    return df[['Population','Share of Swedish-speakers of the population, %','Share of foreign citizens of the population, %']]


def main():
    print(swedish_and_foreigners())
    return

if __name__ == "__main__":
    main()
