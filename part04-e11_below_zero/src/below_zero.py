#!/usr/bin/env python3

import pandas as pd

def below_zero():
    '''this funciton reads the weather data and returns  the number of days when the temperature was below zero'''
    
    df = pd.read_csv('src/kumpula-weather-2017.csv')
    df = df[df['Air temperature (degC)'] < 0]
    des = df.describe()
    return des.loc['count', 'Year']

def main():
    print(f"Number of days below zero: {below_zero():.0f}")
    
if __name__ == "__main__":
    main()
