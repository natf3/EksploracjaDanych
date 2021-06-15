import pandas as pd
import string
import re
import nltk

def remove_punctuation(text):
    text_nopunctuation = "".join([char for char in text if char not in string.punctuation])
    return text_nopunctuation

# ograniczenie liczby wyświetlanych kolumn (dla większej czytelności)
pd.set_option('display.max_colwidth', 100)
data = pd.read_csv('Restaurant_Reviews.tsv', sep='\t', header=None)
data.columns = ['body_text', 'liked']
print(data.head())

data['body_text_clean'] = data['body_text'].apply(lambda text: remove_punctuation(text))

print(data.head())
print(data['body_text_clean'][0:10])

def tokenize(text):
    # '\W+' - reaguje na znaki, które nie są
    # znakami występującymi w słowach
    tokens = re.split('\W+', text)
    return tokens

data['body_text_tokenized'] = data['body_text_clean'].apply(lambda text : tokenize(text.lower()))
print(data['body_text_tokenized'][0:10])

stopword = nltk.corpus.stopwords.words("english")

def remove_stopwords(tokens):
    text = [word for word in tokens if word not in stopword]
    return text

data['body_text_nostop'] = data['body_text_tokenized'].apply(lambda text : remove_stopwords(text))
print(data['body_text_nostop'][0:10])