#!/usr/bin/env python3

import pandas as pd

def snow_depth():
    '''reads the kumpula-weather-2017.csv file and returns the maximum snow depth in the year 2017'''
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    df =  df.describe()
    return df.loc['max', 'Snow depth (cm)']


def main():
    x = snow_depth()
    print(f"Max snow depth: {x:.1f}")

if __name__ == "__main__":
    main()
