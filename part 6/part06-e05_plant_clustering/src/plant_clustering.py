#!/usr/bin/env python3

import scipy
from sklearn.datasets import load_iris
from sklearn import cluster
from sklearn import metrics


def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

def plant_clustering():
    '''this function returns the acuracy of the clustering model on the iris dataset'''
    iris = load_iris()
    X = iris.data
    y = iris.target

    model = cluster.KMeans(n_clusters=3, random_state=0)
    model.fit(X)
    labels = model.labels_
    permutation = find_permutation(3, y, labels)
    labels = [permutation[label] for label in labels]
    return metrics.accuracy_score(y, labels)


def main():
    print(plant_clustering())

if __name__ == "__main__":
    main()
