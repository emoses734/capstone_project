import matplotlib
matplotlib.use('agg')
import os

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


class Analysis ():

    def __init__ (self, directory='reviews'):
        self.data_file = './app/static/data/' + directory + '.csv'
        self.df = pd.read_csv(self.data_file, encoding= 'latin1')

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

    def makeDF(self, filter=None):
        self.df['cleaned words list'] = self.df['review'].apply(self.textLemmatizer)
        self.df['cleaned words'] = self.df['cleaned words list'].apply(self.stringFromList)
        self.df['reviewblob'] = self.df['cleaned words'].apply(TextBlob)

        self.df = self.df.drop(columns = ['Unnamed: 0','reviewblob', 'cleaned words', 'cleaned words list'])
        if filter != None:
            self.df = self.df[self.df['name'].str.match(filter)]

        return self.df.to_html()









# def plotPoints(x,y,xlabel,ylabel,title):
#     fig = plt.figure(figsize=(20,10))
#     plt.plot(x,y,'bo-')
#     plt.title('{}' .format(title), fontsize=36)
#     plt.xlabel('{}' .format(xlabel), fontsize=24)
#     plt.ylabel('{}' .format(ylabel), fontsize=24)
#
#     my_path = os.path.abspath(os.path.dirname(__file__)) + '/static/graph_images/'
#     plot_name = 'test-graph'
#     url = my_path + plot_name
#     fig.savefig(url)
#     return plot_name
