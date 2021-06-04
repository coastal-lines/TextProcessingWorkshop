from sklearn.feature_extraction.text import CountVectorizer
import scipy as sp
import sys

t1="This is a toy post about machine learning. Actually, it contains not much interesting stuff."
t2="Imaging databases provide storage capabilities."
t3="Most imaging databases save images permanently."
t4="Imaging databases store data."
t5="Imaging databases store data. Imaging databases store data. Imaging databases store data."

posts = [t1,t2,t3,t4,t5]
vectorizer = CountVectorizer(min_df=1)
X_train = vectorizer.fit_transform(posts)
num_samples,num_features = X_train.shape
#print("#samples: %d, #features: %d" % (num_samples, num_features))

new_post = "imaging databases"
#use transform instead fit_transform for making array with zeros - we need this for right shapes or arrays
new_post_vec = vectorizer.transform([new_post])


def dist_raw(v1, v2):
    delta = v1 - v2
    return sp.linalg.norm(delta.toarray())

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