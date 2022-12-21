#!/usr/bin/env python3

import pandas as pd

def cyclists():
    '''Reads the data from the file Helsingin_pyorailijamaarat.csv and returns a cleaned DataFrame without the empty rows in the end and the unnecessary columns.'''
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    df = df.dropna(how='all')
    df = df.dropna(axis=1, how='all')
    return df


def main():
    df = cyclists()
    print(df)
    
if __name__ == "__main__":
    main()
