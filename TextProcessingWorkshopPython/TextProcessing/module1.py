from sklearn.feature_extraction.text import CountVectorizer

#convert lines into vector arrays

text1 = "How to format my hard disk"
text2 = "Hard disk format problems"

vectorizer = CountVectorizer(min_df=1)
content = ["How to format my hard disk","Hard disk format problems"]
X = vectorizer.fit_transform(content)
vectorizer.get_feature_names()
print(X.toarray().transpose())