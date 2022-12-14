#!/usr/bin/env python3

import pandas as pd

#!/usr/bin/env python3

import pandas as pd
import numpy as np


def best_record_company():
    '''This function reads the data from the file artists.csv. Return a DataFrame of the singles by the best record company.'''
    df = pd.read_csv('src/UK-top40-1964-1-2.tsv',sep='\t')
    df = df.replace({'Re':np.nan,'New':np.nan})
    df['LW'] = df['LW'].astype(float)

    publishers = df.groupby('Publisher').sum()
    publishers = publishers.sort_values('WoC', ascending=False)
    best_publisher = publishers.index[0]

    return df[df['Publisher'] == best_publisher]

def main():
    df = best_record_company()
    print(df)
    

if __name__ == "__main__":
    main()
