from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk.stem
import scipy as sp
import sys

t1="This is a toy post about machine learning. Actually, it contains not much interesting stuff."
t2="Imaging databases"
t3="Imaging databases provide storage capabilities."
t4="Most imaging databases save images permanently."
t5="Imaging databases store data."
t6="Imaging databases store data. Imaging databases store data. Imaging databases store data."
t7="Imaging databases"
posts = [t1,t2,t3,t4,t5,t6,t7]

vectorizer = None

#загрузка корпуса
def loadInputs():
    corpus = []
    with open(r"C:\Temp2\New folder\DataVisualizationAndStatisticsForRally\Draft\inputsListTxt.txt") as f:
        corpus = f.read().splitlines()

    return corpus

#удаление суффиксов и удаление заглавных
#для проекта плохо подходит! окончания критичны!
def tokenize(corpus):

    #nltk.stem.SnowballStemmer('english') - удаление суффиксов и окончаний
    english_stemmer = nltk.stem.SnowballStemmer('english')

    for i in range(len(corpus)):
        corpus[i] = corpus[i].lower()
        tokens = nltk.word_tokenize(corpus[i])

        newDocument = ""
        for j in range(len(tokens)):
            if ( "." in tokens[j] or "," in tokens[j]):
                newDocument += english_stemmer.stem(tokens[j])
            else:
                newDocument += english_stemmer.stem(tokens[j]) + " "

        corpus[i] = newDocument

    return corpus

def makeTFIDFVectorizer():
    #stop_words='english' - удаление наиболее популярных 318 слов
    return TfidfVectorizer(min_df=1, stop_words='english')

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
    #newPostCleaned = tokenize([newPost])
    newPostVect = tfidfVectorize(vectorizer, [newPost], False)

    results = []
    value = 1
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

        if result < value:
            value = result
            position = i

    print("The most similar is: " + str(value) + " " + str(corpus[position]))

posts = loadInputs()
#cleanedCorpus = tokenize(posts)
vectorizer = makeTFIDFVectorizer()
x_train = tfidfVectorize(vectorizer, posts)
newPost = "Praporshik Zadov"
doCompare(vectorizer, x_train, posts, newPost)

t=0