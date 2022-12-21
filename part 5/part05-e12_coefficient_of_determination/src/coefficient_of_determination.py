#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model


def coefficient_of_determination():
    '''reads the mystery_data.tsv file and returns a list of R2 scores for all x variables and the full model'''
    df = pd.read_csv("src/mystery_data.tsv", sep="\t")
    x = df.iloc[:, :-1]
    y = df.iloc[:, -1]
    model = linear_model.LinearRegression()
    model.fit(x, y)

    ret = [model.score(x, y)]
    for i in x:
        model.fit(x[[i]], y)
        ret.append(model.score(x[[i]], y))
    return ret
    
def main():
    x = coefficient_of_determination()
    print(f"R2-score with feature(s) X: {x[0]}")
    for i in range(1,len(x)):
        print(f"R2-score with feature(s) X{i}: {x[i]}")

if __name__ == "__main__":
    main()
