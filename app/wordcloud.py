import requests
import pandas as pd
import numpy as np
import re
import csv
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import urllib.request
import nltk
import nltk.corpus
from nltk.text import Text
import sys

from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer


class WordCloud ():

        def __init__ (self):
            self.data_file = './app/static/data/reviews.csv'
            self.df = pd.read_csv(self.data_file)

        def stringFromList(self, my_list):
            new_string = ' '.join(my_list)
            return new_string


        def textLemmatizer(self, my_text):

            raw_words = nltk.word_tokenize(my_text)
            # Clean words
            words = [word for word in raw_words if len(word) > 1]
            words = [word for word in words if word.isalpha()]
            words = [w.lower() for w in words if w.isalnum()]
            # Stop words
            stopwords = set(nltk.corpus.stopwords.words('english'))
            # There are plenty of functions that allow us to modify the stopwords.
            words = [word for word in words if word not in stopwords]
            # Lemma or Stem; use Lemmatizer for better results
            wnl = nltk.WordNetLemmatizer()
            cleaned_words = [wnl.lemmatize(t) for t in words]
        #     print(cleaned_words)
            return cleaned_words
