#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score
from sklearn.metrics import pairwise_distances
import scipy

from matplotlib import pyplot as plt

import seaborn as sns
sns.set(color_codes=True)
import scipy.spatial as sp
import scipy.cluster.hierarchy as hc

def toint(x):
    ''' maps the nucleotides to integers'''
    if x == 'A':
        return 0
    elif x == 'C':
        return 1
    elif x == 'G':
        return 2
    elif x == 'T':
        return 3

def toint_str(x):
    '''gets a sequence oi nucleatides and maps the nucleotides to integers'''
    ret = []
    for i in x:
        ret.append(toint(i))
    return ret

def get_features_and_labels(filename):
    ''' the function  load the contents of the file into a DataFrame. The column X contains a string.Convert this column into a feature matrix using the above toint function.'''
    df = pd.read_csv(filename, sep='\t')

    x = df['X'].apply(toint_str).to_numpy()
    y = df['y'].to_numpy()
    x = np.vstack(x)
    return x, y


def find_permutation(n_clusters, real_labels, labels):     
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

def plot(distances, method='average', affinity='euclidean'):
    mylinkage = hc.linkage(sp.distance.squareform(distances), method=method)
    g=sns.clustermap(distances, row_linkage=mylinkage, col_linkage=mylinkage )
    g.fig.suptitle(f"Hierarchical clustering using {method} linkage and {affinity} affinity")
    plt.show()

def cluster_euclidean(filename):
    ''' The function loads a dataset and performs hierarchical clustering using the Euclidean distance and the average linkage. The function returns the accuracy score of the clustering.'''
    X, Y = get_features_and_labels(filename)

    model = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='average')
    model.fit(X)

    labels = model.labels_
    permutation = find_permutation(2, Y, labels)
    labels = np.array([permutation[label] for label in labels])
    return accuracy_score(Y, labels)


def cluster_hamming(filename):
    ''' The function loads a dataset and performs hierarchical clustering using the Hamming distance and the average linkage. The function returns the accuracy score of the clustering.'''
    x, y = get_features_and_labels(filename)
    distances = pairwise_distances(x, metric='hamming')
    model  = AgglomerativeClustering(n_clusters=2, affinity='precomputed', linkage='average')
    model.fit_predict(distances)

    labels = model.labels_
    permutation = find_permutation(2, y, labels)
    labels = np.array([permutation[label] for label in labels])
    return accuracy_score(y, labels)



def main():
    print("Accuracy score with Euclidean affinity is", cluster_euclidean("src/data.seq"))
    print("Accuracy score with Hamming affinity is", cluster_hamming("src/data.seq"))

if __name__ == "__main__":
    main()
