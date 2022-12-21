#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

import pandas as pd

def cyclists():
    '''Reads the data from the file Helsingin_pyorailijamaarat.csv and returns a cleaned DataFrame without the empty rows in the end and the unnecessary columns.'''
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    df = df.dropna(how='all')
    df = df.dropna(axis=1, how='all')
    df_orig = df.copy()
    return df_orig, df

def split_date():
    '''Splits the Päivämäärä column into a DataFrame with five columns with column names Weekday, Day, Month, Year, and Hour. Day, Month, and Year are integers and Hour and Weekday are strings.'''
    df_orig, df = cyclists()

    df = df['Päivämäärä'].str.split(expand=True)

    df.columns = ['Weekday', 'Day', 'Month', 'Year', 'Hour']

    day_dic = {'ma': 'Mon', 'ti': 'Tue', 'ke': 'Wed', 'to': 'Thu', 'pe': 'Fri', 'la': 'Sat', 'su': 'Sun'}
    month_dic = {'tammi': 1, 'helmi': 2, 'maalis': 3, 'huhti': 4, 'touko': 5, 'kesä': 6, 'heinä': 7, 'elo': 8, 'syys': 9, 'loka': 10, 'marras': 11, 'joulu': 12}
    df['Weekday'] = df['Weekday'].map(day_dic)
    df['Month'] = df['Month'].map(month_dic)
    
    df['Hour'] = df['Hour'].str.split(':', expand=True)[0].astype(int)
    df = df.astype({'Day': int, 'Month': int, 'Year': int, 'Hour': int})

    return df_orig, df

def split_date_continues():
    '''This function reads the cleaned bycical dataset and drops the päivämäärä column to replace it with its splited componenets'''
    df_orig, df = split_date()
    df_orig = df_orig.drop('Päivämäärä', axis=1)
    ret_df = pd.concat([df, df_orig], axis=1)
    return ret_df

def cyclists_per_day():
    '''This function reads the cleaned bycical dataset and returns a DataFrame with the total number of cyclists per day'''
    df = split_date_continues()
    df = df.drop(['Hour', 'Weekday'], axis=1)
    df = df.groupby(['Year', 'Month', 'Day']).sum()
    return df
    
def main():
    '''This function calls the cyclists_per_day function and restrics teh data to august 2017. Finally we plot the data'''
    df = cyclists_per_day()
    df = df.loc[2017, 8]
    df.plot()
    plt.show()

if __name__ == "__main__":
    main()
