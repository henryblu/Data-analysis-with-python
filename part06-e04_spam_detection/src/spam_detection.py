#!/usr/bin/env python3
import gzip
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


def spam_detection(random_state=0, fraction=0.1):
    """ This function reads a smap and ham data set. It then  vectorizes the data and splits it into a training and test set. and finally trains a Multinomial Naive Bayes model on the data. It returns the accuracy of the model, the total number of messages and the number of misclassified messages."""

    with gzip.open("src/spam.txt.gz", "rt") as f:
        spam = f.readlines()
    spam = spam[:int(len(spam) * fraction)]

    with gzip.open("src/ham.txt.gz", "rt") as f:
        ham = f.readlines()
    ham = ham[:int(len(ham) * fraction)]
	

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(ham + spam).toarray()
    y = np.array([0] * len(ham) + [1] * len(spam))

    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.75, random_state=random_state)
    model = MultinomialNB()
    model.fit(X_train, y_train)

    prediction = model.predict(X_test)

    accuracy = accuracy_score(y_test, prediction)
    total = len(y_test)
    misclassified = total - accuracy * total

    return accuracy, total, misclassified


def main():
    accuracy, total, misclassified = spam_detection()
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")

if __name__ == "__main__":
    main()
