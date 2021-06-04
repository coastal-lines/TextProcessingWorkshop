from sklearn.feature_extraction.text import CountVectorizer
import scipy as sp
import sys

text = []
with open(r"C:\Temp2\New folder\DataVisualizationAndStatisticsForRally\Draft\inputsListTxt.txt") as f:
    text = f.read().splitlines()

#posts = [t1,t2,t3,t4,t5]
vectorizer = CountVectorizer(min_df=1)
X_train = vectorizer.fit_transform(text)
num_samples,num_features = X_train.shape
#print("#samples: %d, #features: %d" % (num_samples, num_features))

new_post = "finish экзам"
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

    for i, post in enumerate(text):
        post = text[i]
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

    for i, post in enumerate(text):
        post = text[i]
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
t=0