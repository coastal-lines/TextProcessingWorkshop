from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk.stem
import scipy as sp
import sys

vectorizer = None
newPost = "last name"

#загрузка корпуса
def loadInputs():
    corpus = []
    with open(r"C:\Temp2\New folder\DataVisualizationAndStatisticsForRally\Draft\inputsListTxt2.txt") as f:
        corpus = f.read().splitlines()

    return corpus

def makeTFIDFVectorizer():
    return TfidfVectorizer(min_df=1)

def tfidfVectorize(vectorizer, corpus, isFit = True):
    if (isFit):
        x_train = vectorizer.fit_transform(corpus)
    else:
        x_train = vectorizer.transform(corpus)

    return x_train

def distanceBeetwenVectors(v1, v2):
    v1_normalized = v1 / sp.linalg.norm(v1.toarray())
    v2_normalized = v2 / sp.linalg.norm(v2.toarray())
    delta = v1_normalized - v2_normalized
    return sp.linalg.norm(delta.toarray())

def doCompare(vectorizer, x_train, corpus, newPost):
    newPostVect = tfidfVectorize(vectorizer, [newPost], False)

    results = []
    value = None
    position = None
    for i in range(x_train.shape[0]):
        if(newPost == corpus[i]):
            result = 0
            results.append(result)
            print(str(result) + " ..... " + corpus[i])
            value = 0
            position = i
            continue

        result = distanceBeetwenVectors(x_train[i], newPostVect)
        results.append(result)
        print(str(result) + " ..... " + corpus[i])

        if (i == 0):
            value = result

        if result < value:
            value = result
            position = i

        if (position == None):
            position = 0

    print("The most similar is: " + str(value) + " " + str(corpus[position]) + " | " + str(newPost))

posts = loadInputs()
vectorizer = makeTFIDFVectorizer()
x_train = tfidfVectorize(vectorizer, posts)
doCompare(vectorizer, x_train, posts, newPost)

#можно добавить проверку по каждому слову в найденном тексте и если слово есть, то убавлять от результата