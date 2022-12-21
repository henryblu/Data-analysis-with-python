#!/usr/bin/env python3

import pandas as pd
import numpy as np


def cleaning_data():
    '''This function Reads the presidents.tsv file and cleans the data.'''

    df = pd.read_csv('src/presidents.tsv', sep='\t')
    df.columns=["President", "Start", "Last", "Seasons", "Vice-president"]

    # First we clean the President column and Vice-president column. if the name has a comma, we switch the order of the names
    df["President"] = df["President"].str.replace(r"(\w+), *(\w+)", r"\2 \1").str.title()
    df["Vice-president"] = df["Vice-president"].str.replace(r"(\w+), *(\w+)", r"\2 \1").str.title()

    # Then we clean the Start column
    df['Start'] = df['Start'].str.split(' ').str[0].astype(int)

    # Then we clean the Last column
    df["Last"] = df["Last"].replace("-", np.nan).astype(float)

    # Finally we clean the Seasons column
    print_to_int = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    df['Seasons'] = df['Seasons'].replace(print_to_int).astype(int)

    return df

def main():
    df = cleaning_data()
    print(df)

if __name__ == "__main__":
    main()
