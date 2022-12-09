#!/usr/bin/env python3

import pandas as pd
import numpy as np

def cyclists():
    '''Reads the data from the file Helsingin_pyorailijamaarat.csv and returns a cleaned DataFrame without the empty rows in the end and the unnecessary columns.'''
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    df = df.dropna(how='all')
    df = df.dropna(axis=1, how='all')
    return df

def split_date():
    '''Splits the Päivämäärä column into a DataFrame with five columns with column names Weekday, Day, Month, Year, and Hour. Day, Month, and Year are integers and Hour and Weekday are strings.'''
    df = cyclists()
    df = df['Päivämäärä'].str.split(expand=True)
    df.columns = ['Weekday', 'Day', 'Month', 'Year', 'Hour']
    df.loc[df['Weekday'] == 'ma', 'Weekday'] = 'Mon'
    df.loc[df['Weekday'] == 'ti', 'Weekday'] = 'Tue'
    df.loc[df['Weekday'] == 'ke', 'Weekday'] = 'Wed'
    df.loc[df['Weekday'] == 'to', 'Weekday'] = 'Thu'
    df.loc[df['Weekday'] == 'pe', 'Weekday'] = 'Fri'
    df.loc[df['Weekday'] == 'la', 'Weekday'] = 'Sat'
    df.loc[df['Weekday'] == 'su', 'Weekday'] = 'Sun'
    df.loc[df['Month'] == 'tammi', 'Month'] = 1
    df.loc[df['Month'] == 'helmi', 'Month'] = 2
    df.loc[df['Month'] == 'maalis', 'Month'] = 3
    df.loc[df['Month'] == 'huhti', 'Month'] = 4
    df.loc[df['Month'] == 'touko', 'Month'] = 5
    df.loc[df['Month'] == 'kesä', 'Month'] = 6
    df.loc[df['Month'] == 'heinä', 'Month'] = 7
    df.loc[df['Month'] == 'elo', 'Month'] = 8
    df.loc[df['Month'] == 'syys', 'Month'] = 9
    df.loc[df['Month'] == 'loka', 'Month'] = 10
    df.loc[df['Month'] == 'marras', 'Month'] = 11
    df.loc[df['Month'] == 'joulu', 'Month'] = 12
    df['Hour'] = df['Hour'].str.split(':', expand=True)[0].astype(int)
    df = df.astype({'Day': int, 'Month': int, 'Year': int, 'Hour': int})
    return df

def main():
    df = split_date()
    print(df)
    
       
if __name__ == "__main__":
    main()
