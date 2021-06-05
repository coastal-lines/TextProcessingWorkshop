from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import scipy as sp
import sys
import nltk.stem

#загружаем предложения
#переводим их в векторное представление
#убираем лишние слова
#применяем стеммер - вычленяем только корни слов
#применяем tf-idf

english_stemmer = nltk.stem.SnowballStemmer('english')

class StemmedCountVectorizer(CountVectorizer):
    def build_analyzer(self):
        analyzer = super(StemmedCountVectorizer, self).build_analyzer()


        return lambda doc: (english_stemmer.stem(w) for w in analyzer(doc))

class StemmedTfidfVectorizer(TfidfVectorizer):

    def build_analyzer(self):
        analyzer = super(StemmedTfidfVectorizer, self).build_analyzer()
        return lambda doc: (english_stemmer.stem(w) for w in analyzer(doc))

t1="This is a toy post about machine learning. Actually, it contains not much interesting stuff."
t2="Imaging databases provide storage capabilities."
t3="Most imaging databases save images permanently."
t4="Imaging databases store data."
t5="Imaging databases store data. Imaging databases store data. Imaging databases store data."

posts = [t1,t2,t3,t4,t5]
#vectorizer = CountVectorizer(min_df=1, stop_words='english')
#vectorizer = StemmedCountVectorizer(min_df=1, stop_words='english')
vectorizer = StemmedTfidfVectorizer(min_df=1, stop_words='english', decode_error='ignore')
X_train = vectorizer.fit_transform(posts)
num_samples,num_features = X_train.shape
#print("#samples: %d, #features: %d" % (num_samples, num_features))

new_post = "imaging databases"
#use transform instead fit_transform for making array with zeros - иначе отбрасываются нули и в дальнейшем нельзя использовать вектора разного размера
new_post_vec = vectorizer.transform([new_post])


#нормируем вектора - делим вектор на нормированное значение
def dist_norm(v1, v2):
    v1_normalized = v1 / sp.linalg.norm(v1.toarray())
    v2_normalized = v2 / sp.linalg.norm(v2.toarray())
    delta = v1_normalized - v2_normalized
    return sp.linalg.norm(delta.toarray())

def simpleCompare():
    best_dist = sys.maxsize
    best_i = None

    for i, post in enumerate(posts):
        post = posts[i]
        if post == new_post:
            continue
        post_vec = X_train.getrow(i)
        d = dist_raw(post_vec, new_post_vec)

        print("=== Post %i with dist=%.2f: %s" % (i, d, post))

        if d < best_dist:
            best_dist = d
            best_i = i

    print("Best post is %i with dist=%.2f" % (best_i, best_dist))

def normalizedCompare():
    best_dist = sys.maxsize
    best_i = None

    for i, post in enumerate(posts):
        post = posts[i]
        if post == new_post:
            continue
        post_vec = X_train.getrow(i)
        d = dist_norm(post_vec, new_post_vec)

        print("=== Post %i with dist=%.2f: %s" % (i, d, post))

        if d < best_dist:
            best_dist = d
            best_i = i

    print("Best post is %i with dist=%.2f" % (best_i, best_dist))

normalizedCompare()