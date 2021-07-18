from sklearn.feature_extraction.text import CountVectorizer
import scipy as sp
import numpy as np
import sys

str = ["one"]
vectorizer = CountVectorizer(min_df=1)
v1 = vectorizer.fit_transform(str)

str = ["on"]
v2 = vectorizer.fit_transform(str)


v1 = ["1","1","1:"].toarray()
v2 = ["1","1","1"].toarray()
delta = v1 - v2
print(sp.linalg.norm(delta.toarray()))