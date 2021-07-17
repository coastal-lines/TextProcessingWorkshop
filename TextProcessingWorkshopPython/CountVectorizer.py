from sklearn.feature_extraction.text import CountVectorizer

#создаём счетчик слов, который преобразует строку в вектор
#параметр означает минимальное число вхождения слова, т.е. если =10, то если слово встретилось 9 раз, то оно исключается
#можно использовать дроби - будет процентное соотношение
vectorizer = CountVectorizer(min_df=1)
#строки
content = ["How to format my hard disk", "Hard disk format problems"]
#конвертируем строки в матрицу счетчиков токенов
X = vectorizer.fit_transform(content)


print(vectorizer.get_feature_names())
print(X.toarray().transpose())
print(X.toarray())