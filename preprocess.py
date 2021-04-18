import numpy as np
import pandas as pdb
import os
import re
import nltk
from nltk.stem import WordNetLemmatizer 
from nltk.corpus import stopwords
nltk.download('wordnet')

def concate(title, author, text):
    total = title+author+text
    total = [total]
    return total

def cleaning(sentence):
    stop_words = set(stopwords.words('english'))
    filter_sentence = ''
    lemmatizer = WordNetLemmatizer()
    sentence = re.sub(r'[^\w\s]','',str(sentence))
    words = nltk.word_tokenize(sentence)
    words = [w for w in words if not w in stop_words]
    for word in words:
        filter_sentence = filter_sentence + ' ' + str(lemmatizer.lemmatize(word)).lower()
    return filter_sentence