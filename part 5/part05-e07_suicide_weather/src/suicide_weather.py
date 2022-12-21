#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():
    '''this function loads the dataset suicide_fractions from the src folder. It returns a Series that has the country as the row index and the mean fraction of suicides per population as the coulmns'''

    df = pd.read_csv('src/who_suicide_statistics.csv', index_col='country')
    df['fraction']=df['suicides_no']/df['population']
    means = df.groupby('country')[['fraction']].mean()

    return pd.Series(means['fraction'])

def suicide_weather():
    '''reads the List_of_countries_by_average_yearly_temperature file from the src folder and meerges it with the dataframe from suicie fractions. Finally it will find the spearman correlation value betweenm the suicide fraction and the temperature on a day '''
    df1 = suicide_fractions()
    df = pd.read_html("src/List_of_countries_by_average_yearly_temperature.html", index_col="Country")[0]
    df.rename(columns={"Average yearly temperature (1961–1990, degrees Celsius)":"TempAvg"}, inplace=True)
    df = pd.to_numeric(df.iloc[:, 0].str.replace("\u2212", "-"))

    common_rows = pd.concat([df1, df], axis=1, join="inner")
    Spearman_corr = common_rows["fraction"].corr(common_rows["TempAvg"], method="spearman")
    return (len(df1), len(df), len(common_rows), Spearman_corr)

def main():
    '''prints out the results from the suicide weather function'''
    ans = suicide_weather()
    print(f'Suicide DataFrame has {ans[0]} rows')
    print(f'Temperature DataFrame has {ans[1]} rows')
    print(f'Common DataFrame has {ans[2]} rows')
    print(f'Spearman correlation: {ans[3]} rows')
    

if __name__ == "__main__":
    main()



