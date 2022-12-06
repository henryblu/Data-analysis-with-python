#!/usr/bin/env python3

import pandas as pd

def municipalities_of_finland():
    '''Takes in a municipal dataframe. Returns a DataFrame containing only rows about municipalities.'''
    df = pd.read_csv("src/municipal.tsv", sep="\t", index_col="Region 2018")
    return df['Akaa':'Äänekoski']
    
def main():
    #df = pd.read_csv("src/municipal.tsv", sep="\t", index_col="Region 2018")
    print(municipalities_of_finland())
    return
    
if __name__ == "__main__":
    main()
