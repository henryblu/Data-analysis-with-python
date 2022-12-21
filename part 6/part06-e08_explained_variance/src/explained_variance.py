#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn.decomposition import PCA
import pandas as pd

def explained_variance():
    '''The function reads the data from the file src/data.tsv and returns the variances of the columns and the explained variances after PCA.'''
    df = pd.read_csv("src/data.tsv", sep='\t')
    var = df.var(axis=0)
    X = df.to_numpy()
    pca = PCA(n_components=10)
    pca.fit(X)
    return var, pca.explained_variance_


def main():
    
    v, ev = explained_variance()
    v_list = " ".join([f"{x:.3f}" for x in v])
    ev_list = " ".join([f"{x:.3f}" for x in ev])

    print(f"The variances are: {v_list}")
    print(f"The explained variances after PCA are: {ev_list}")

    sum = np.cumsum(ev)
    terms = len(sum)

    plt.plot(np.arange(1, terms + 1), sum)
    plt.show()


if __name__ == "__main__":
    main()
