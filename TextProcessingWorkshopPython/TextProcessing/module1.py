from sklearn.feature_extraction.text import CountVectorizer

#шаг 1
#convert lines into vector arrays
#перевод предложений в вектора

text1 = "How to format my hard disk"
text2 = "Hard disk format problems"

vectorizer = CountVectorizer(min_df=1)
content = ["How to format my hard disk","Hard disk format problems"]
X = vectorizer.fit_transform(content)
print(len(X.shape[0]))
print(len(vectorizer.get_feature_names()))
print(X.toarray().transpose())