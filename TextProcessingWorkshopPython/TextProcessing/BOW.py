from sklearn.feature_extraction.text import CountVectorizer

bards_words = ["The fool doth think hi is wise,", "but the wise man knows himself to be a fool"]
vect = CountVectorizer()
vect.fit(bards_words)
print("Size of dictanary: {}".format(len(vect.vocabulary_)))
print("Content of dictanary: \n {}".format(vect.vocabulary_))
bag_of_words = vect.transform(bards_words)
print("bag_of_words: {}".format(repr(bag_of_words)))
print("bag_of_words: \n {}".format(bag_of_words.toarray()))