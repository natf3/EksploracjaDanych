# import pandas as pd
# import nltk
# import re
# import string
# ps = nltk.PorterStemmer()
# stopwords = nltk.corpus.stopwords.words('english')
# data = pd.read_csv("SMSSpamCollection.tsv", sep='\t')
# data.columns = ['label', 'body_text']
# print(data.head())

# def clean_text(text):
#     text = "".join([word for word in text if word not in string.punctuation])
#     tokens = re.split('\W+', text)
#     text = [word for word in tokens if word not in stopwords]
#     return text

# data['body_text_nostop'] = data['body_text'].apply(lambda x: clean_text(x.lower()))

# print(data.head())

# def stemming(tokenized_text):
#     text = [ps.stem(word) for word in tokenized_text]
#     return text

# data['body_text_stemmed'] = data['body_text_nostop'].apply(lambda x: stemming(x))
# print(data.head())

import nltk
wn = nltk.WordNetLemmatizer()
ps = nltk.PorterStemmer() # do testowania
# print(ps.stem('meanness'))
# print(ps.stem('meaning'))
# print(wn.lemmatize('meanness'))
# print(wn.lemmatize('meaning'))
print(ps.stem('goose'))
print(ps.stem('geese'))
print(wn.lemmatize('goose'))
print(wn.lemmatize('geese'))
