from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk.stem

t1="This is a toy post about machine learning. Actually, it contains not much interesting stuff."
t2="Imaging databases provide storage capabilities."
t3="Most imaging databases save images permanently."
t4="Imaging databases store data."
t5="Imaging databases store data. Imaging databases store data. Imaging databases store data."
posts = [t1,t2,t3,t4,t5]

#загрузка корпуса
def loadInputs():
    corpus = []
    with open(r"C:\Temp2\New folder\DataVisualizationAndStatisticsForRally\Draft\inputsListTxt.txt") as f:
        corpus = f.read().splitlines()

    return corpus

#удаление суффиксов и удаление заглавных
def tokenize(corpus):
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

def countVectorize(corpus):
    vectorizer = CountVectorizer(min_df=1)
    x_train = vectorizer.fit_transform(corpus)
    return x_train

def tfidfVectorize(corpus):
    vectorizer = TfidfVectorizer(min_df=1)
    x_train = vectorizer.fit_transform(corpus)
    return x_train

cleanedCorpus = tokenize(posts)
x_train = doVectorize(cleanedCorpus)
t=0