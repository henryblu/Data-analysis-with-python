#!/usr/bin/env python3

from collections import Counter
import urllib.request
from lxml import etree

import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn import model_selection

alphabet="abcdefghijklmnopqrstuvwxyzäö-"
alphabet_set = set(alphabet)

# Returns a list of Finnish words
def load_finnish():
    finnish_url="https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename="src/kotus-sanalista_v1.xml"
    load_from_net=False
    if load_from_net:
        with urllib.request.urlopen(finnish_url) as data:
            lines=[]
            for line in data:
                lines.append(line.decode('utf-8'))
        doc="".join(lines)
    else:
        with open(filename, "rb") as data:
            doc=data.read()
    tree = etree.XML(doc)
    s_elements = tree.xpath('/kotus-sanalista/st/s')
    return list(map(lambda s: s.text, s_elements))

def load_english():
    with open("src/words", encoding="utf-8") as data:
        lines=map(lambda s: s.rstrip(), data.readlines())
    return lines

def get_features(a):
    '''gets a one dimensional np.array, containing words, as parameter. returns a two dimensional np.array, number of times the corresponding character appears in the word.
    '''
    features = np.zeros((len(a), len(alphabet)))
    for i, word in enumerate(a):
        for j, char in enumerate(alphabet):
            features[i, j] += word.count(char)
    return features

def contains_valid_chars(s):
    '''gets a string as parameter. returns True if the string contains only characters in alphabet, False otherwise'''
    for char in s:
        if char not in alphabet_set:
            return False
    return True

def get_features_and_labels():
    '''returns a tuple of two np.arrays. the first array contains the features, the second array contains the labels. the labels are 0 for Finnish words and 1 for English words. '''
    finnish = load_finnish()
    english = load_english()

    finnish = list(map(lambda s: s.lower(), finnish))
    english = list(filter(lambda s: s[0].islower(), english))
    english = list(map(lambda s: s.lower(), english))

    finnish = list(filter(contains_valid_chars, finnish))
    english = list(filter(contains_valid_chars, english))

    features = get_features(np.array(finnish + english))
    labels = np.array([0] * len(finnish) + [1] * len(english))
    return features, labels


def word_classification():
    '''returns a list of accuracy scores for the model'''
    features, labels = get_features_and_labels()
    model = MultinomialNB()
    gen = model_selection.KFold(n_splits=5, shuffle=True, random_state=0)
    scores = cross_val_score(model, features, labels, cv=gen)
    return scores



def main():
    print("Accuracy scores are:", word_classification())

if __name__ == "__main__":
    main()
