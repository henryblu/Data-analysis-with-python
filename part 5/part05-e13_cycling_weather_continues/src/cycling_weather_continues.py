#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

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
    df_orig.drop('Päivämäärä', axis=1, inplace=True)
    df_orig.dropna(axis=0, how='all', inplace=True)
    df_orig.dropna(axis=1, how='all', inplace=True)

    ret_df = pd.concat([df, df_orig], axis=1)

    ret_df = ret_df[ret_df["Year"]==2017] #Limited to 2017 Year
    ret_df = ret_df.groupby(["Day","Month","Year"]).sum().reset_index() #
    ret_df.reset_index()

    return ret_df

def cycling_weather():
    '''This function reads the cleaned bycical dataset and merges it with the cleaned weather dataset'''
    df1 = pd.read_csv('src/kumpula-weather-2017.csv')
    df2 = split_date_continues()
    df = pd.merge(df1, df2, left_on=['Year', 'm', 'd'], right_on=['Year', 'Month', 'Day'])
    df.drop(['m', 'd', 'Time', 'Time zone'], axis=1, inplace = True)
    df = df.fillna(method='ffill')
    return df

def cycling_weather_continues(station):
    '''This function takes in a station name and returns regression coefficients for the station. The independant variables are the "precipitation amount (mm)", "snow depth (cm)", and "Air temperature (degC)". '''
    df = cycling_weather()
    x = df[['Precipitation amount (mm)', 'Snow depth (cm)', 'Air temperature (degC)']]
    y = df[[station]]
    model = linear_model.LinearRegression(fit_intercept=True)
    model.fit(x, y)
    
    return model.coef_[0], model.score(x, y)
    
def main():
    station = 'Baana'
    r, score = cycling_weather_continues(station)
    print(f"Measuring station: {station}")
    print(f"Regression coefficient for variable 'precipitation': {r[0]:.1f}")
    print(f"Regression coefficient for variable 'snow depth': {r[1]:.1f}")
    print(f"Regression coefficient for variable 'temperature': {r[2]:.1f}")
    print(f"Score: {score:.2f}")


if __name__ == "__main__":
    main()

