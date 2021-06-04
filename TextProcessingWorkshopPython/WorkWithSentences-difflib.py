from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
from nltk.corpus import stopwords
import difflib
from textblob import TextBlob

myText = "start exam"

def similarity(s1, s2):
  normalized1 = s1.lower()
  normalized2 = s2.lower()
  matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
  return matcher.ratio()

text = []
with open(r"C:\Temp2\New folder\DataVisualizationAndStatisticsForRally\Draft\inputsListTxt.txt") as f:
    text = f.read().splitlines()

rationList = []
for line in text:
    rationList.append(similarity(myText, line))

max = max(rationList)
pos = rationList.index(max)
print(text[pos])