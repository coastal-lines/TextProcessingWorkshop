from sklearn.feature_extraction.text import CountVectorizer
import scipy as sp
import sys

t1="This is a toy post about machine learning."
t2="last name"

posts = [t1,t2]
vectorizer = CountVectorizer(min_df=1)
X_train = vectorizer.fit_transform(posts)
num_samples,num_features = X_train.shape
#print("#samples: %d, #features: %d" % (num_samples, num_features))

new_post = "zadov"
#use transform instead fit_transform for making array with zeros - иначе отбрасываются нули и в дальнейшем нельзя использовать вектора разного размера
new_post_vec = vectorizer.transform([new_post])

#нормализация - складываем квадраты всех членов и извлекаем корень из суммы
#просто пример
c = [3,2,1]
norm_c = sp.linalg.norm(c)

#из вектора текста вычитаем вектор нового текста
#и нормируем (вычисляется евклидова норма)
#чем меньше полученное значение, тем меньше разница между строками
#проблема - не учитывается повторяемость слов
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