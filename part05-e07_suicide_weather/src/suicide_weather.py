#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():
    '''this function loads the dataset suicide_fractions from the src folder. It returns a Series that has the country as the row index and the mean fraction of suicides per population as the coulmns'''

    df = pd.read_csv('src/who_suicide_statistics.csv', index_col='country')
    df['fraction']=df['suicides_no']/df['population']
    means = df.groupby('country')[['fraction']].mean()

    return pd.Series(means['fraction'])

def suicide_weather():
    '''print hello world'''
    print()
    return (0, 0, 0, 0.0)

def main():
    return

if __name__ == "__main__":
    main()
