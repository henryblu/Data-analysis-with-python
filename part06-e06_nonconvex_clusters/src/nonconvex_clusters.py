#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score
import scipy


def find_permutation(n_clusters, real_labels, labels):

    permutation = []
    if n_clusters == len(real_labels.unique()):
        for i in range(n_clusters):
            idx = labels == i
            # Choose the most common label among data points in the cluster
            new_label = scipy.stats.mode(real_labels[idx])[0][0]
            permutation.append(new_label)
    return permutation





def nonconvex_clusters():
    ''' This function reads the data from the file src/data.tsv
    and returns a DataFrame with the following columns:
    eps: the value of epsilon used in DBSCAN
    Score: the accuracy score of the clustering
    Clusters: the number of clusters found by DBSCAN
    Outliers: the number of outliers found by DBSCAN
    '''
    df = pd.read_csv('src/data.tsv', sep='\t')
    scores = pd.DataFrame(columns=['eps', 'Score', 'Clusters', 'Outliers'], dtype= float)

    eps_val = np.arange(0.05, 0.2, 0.05)

    for eps in eps_val:
        model = DBSCAN(eps=eps)
        model.fit(df[['X1', 'X2']])
        clusters = len(set(model.labels_)) - (1 if -1 in model.labels_ else 0)
        outliers = list(model.labels_).count(-1)

        if clusters == len(df['y'].unique()):
            permutation = find_permutation(clusters, df['y'], model.labels_)
            new_labels = [permutation[label] for label in model.labels_ if label != -1]
            score = accuracy_score(df['y'][model.labels_ != -1], new_labels)
        else:
            score = np.nan

        scores = scores.append({'eps': eps, 'Score': score, 'Clusters': clusters, 'Outliers': outliers}, ignore_index=True)

    return scores


def main():
    print(nonconvex_clusters())

if __name__ == "__main__":
    main()
