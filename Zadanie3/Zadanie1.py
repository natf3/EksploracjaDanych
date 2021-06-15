import pandas as pd
import nltk
import re
import string
ps = nltk.PorterStemmer()
from sklearn.feature_extraction.text import CountVectorizer
from nltk import ngrams
from sklearn.feature_extraction.text import TfidfVectorizer

stopwords = nltk.corpus.stopwords.words('english')

text = ['Star light, start bright,', 
        'The first star I see tonight;',
        'I wish I may, I wish I might,',
        'Have the wish I wish tonight.']

count_vect = CountVectorizer()

result = count_vect.fit_transform(text)
print("CountVetorizer: ")
print(count_vect.get_feature_names())
print(result.shape)
print(result.toarray())

def clean_text(text):    
    text = "".join([word for word in text if word not in string.punctuation])    
    tokens = re.split('\W+', text)
    text = [word for word in tokens if word not in stopwords] 
    text ="".join([ps.stem(word) for word in tokens if word not in stopwords])    
    return text

ngram = CountVectorizer(analyzer='word', ngram_range=(2,2))
print("N-Grams")
result = ngram.fit_transform(text)
print(ngram.get_feature_names())
print(result.shape)
print(result.toarray())

tfidf = TfidfVectorizer(analyzer=clean_text)
result = tfidf.fit_transform(text)
print("TF-IDF")
print(result.shape)
print(result.toarray())

