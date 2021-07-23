import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import scipy as sp
import sys
from nltk.stem.snowball import SnowballStemmer

def loadText():
    with open(r'C:\Temp\!my\TestText.txt') as file:
        text = file.read().split('\n')
        return text

def makeCountVectorizer():
    return CountVectorizer(min_df=1)

def makeCountVectorizerWithStopWords():
    #можно передать свой собственный список
    return CountVectorizer(min_df=1, stop_words='english')

def makeCountVectorizerWithStemmer(text):
    english_stemmer = SnowballStemmer('english')

    for token in nltk.word_tokenize(text):
        yield english_stemmer.stem(token)
    return CountVectorizer(analyzer=text)

def makeTFIDFVectorizer():
    return TfidfVectorizer(min_df=1)

def prepareVocabulary(vectorizer, corpus):
    vocabulary = vectorizer.fit(corpus)
    print(vocabulary.vocabulary_)
    return vocabulary

def transformVocabulary(vectorizer, corpus):
    transformedVocabulary = vectorizer.transform(corpus)
    print(transformedVocabulary.toarray())
    return transformedVocabulary

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

text = loadText()
vectorizer = makeCountVectorizer()
vocabulary = prepareVocabulary(vectorizer, text)
transformedVocabulary = transformVocabulary(vectorizer, ['four, one'])