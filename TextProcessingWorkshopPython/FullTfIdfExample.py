from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import scipy as sp
import numpy as np
import sys

def loadText():
    with open(r'C:\Temp\!my\TestText.txt') as file:
        text = file.read()
        return text

def makeCountVectorizer():
    return CountVectorizer(min_df=1)

def makeTFIDFVectorizer():
    return TfidfVectorizer(min_df=1)

def trainData(vectorizer, corpus):
    return vectorizer.fit(corpus)

def transformDataByModel(vectorizer, corpus):
    return vectorizer.transform(corpus)

def calculateDistantionBetweenVectors(v1, v2):
    v1_normalized = v1 / sp.linalg.norm(v1.toarray())
    v2_normalized = v2 / sp.linalg.norm(v2.toarray())
    delta = v1_normalized - v2_normalized
    return sp.linalg.norm(delta.toarray())

def returnBestThreeResultsAfterSearching(data, new_data, new_data_vec, x_train):
    best_dist = sys.maxsize
    best_i = None

    for i, post in enumerate(data):
        post = data[i]
        if post == new_data:
            continue
        post_vec = x_train.getrow(i)
        d = calculateDistantionBetweenVectors(post_vec, new_data_vec)

        print("=== Post %i with dist=%.2f: %s" % (i, d, post))

        if d < best_dist:
            best_dist = d
            best_i = i

    print("Best post is %i with dist=%.2f" % (best_i, best_dist))

