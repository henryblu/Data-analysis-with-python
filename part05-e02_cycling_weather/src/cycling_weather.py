#!/usr/bin/env python3

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

def cycling_weather():
    '''This function reads the cleaned bycical dataset and merges it with the cleaned weather dataset'''
    df1 = pd.read_csv('src/kumpula-weather-2017.csv')
    df2 = split_date_continues()
    df = pd.merge(df1, df2, left_on=['d', 'm', 'Year'], right_on=['Day', 'Month', 'Year'])
    df = df.drop(['d', 'm', 'Time', 'Time zone'], axis=1)
    return df

def main():
    df = cycling_weather()
    print("Shape:", df.shape)
    print("Column names:\n", df.columns)
    print(df.head())


if __name__ == "__main__":
    main()
