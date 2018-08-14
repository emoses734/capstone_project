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


class Index ():

        def __init__ (self):
                self.data_file = 'reviews'
                self.df = None

        def selectCity(self, string):
            if string == 'somerville':
                self.data_file = './app/static/data/somerville_reviews.csv'

            elif string == 'boston':
                self.data_file = './app/static/data/boston_reviews.csv'
            else:
                pass
