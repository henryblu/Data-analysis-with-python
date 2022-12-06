#!/usr/bin/env python3

import pandas as pd

def average_temperature():
    '''function average_temperature reads the weather data set and returns the average temperature in July.'''
    df = pd.read_csv('src/kumpula-weather-2017.csv')
    df = df.loc[df['m'] == 7]
    sum = df.describe()
    return sum.loc['mean', 'Air temperature (degC)']

def main():
    x = average_temperature()
    print(f"Average temperature in July: {x:.1f}")

if __name__ == "__main__":
    main()
