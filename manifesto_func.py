# import statements
import json
from manifesto import *
from bs4 import BeautifulSoup
from improved_cache_v1 import *
import requests
import textract
from datetime import datetime


# pip install matplotlib
# pip install pandas
# pip install wordcloud

# Python program to generate WordCloud

# importing all necessery modules
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

def word_cloud_roof():
    with open ("manifesto-roof.json", 'r') as f:
        roof_manifesto = json.load(f)
    roof_text = roof_manifesto['Dylan Roof']['Dylan Roof Manifesto']

    comment_words = ' '
    stopwords = set(STOPWORDS)

    tokens = roof_text.split()

    for i in range (len(tokens)):
        tokens[i] = tokens[i].lower()
    for words in tokens:
        comment_words = comment_words + words + ' '
    # print(comment_words)
    wordcloud = WordCloud(width = 800, height = 800,
                    background_color ='black',
                    stopwords = stopwords,
                    min_font_size = 10).generate(comment_words)
    # plot the WordCloud image
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud,  interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout(pad = 0)
    plt.show()


def word_cloud_rodger():
    with open ("manifesto-rodger.json", 'r') as f:
        rodger_manifesto = json.load(f)
    rodger_text = rodger_manifesto['Elliot Rodger']['The Twisted World: The Story of Elliot Rodger']

    comment_words = ' '
    stopwords = set(STOPWORDS)

    tokens = rodger_text.split()

    for i in range (len(tokens)):
        tokens[i] = tokens[i].lower()
    for words in tokens:
        comment_words = comment_words + words + ' '
    # print(comment_words)
    wordcloud = WordCloud(width = 800, height = 800,
                    background_color ='black',
                    stopwords = stopwords,
                    min_font_size = 10).generate(comment_words)
    # plot the WordCloud image
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud,  interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout(pad = 0)
    plt.show()


def word_cloud_cho():
    with open ("manifesto-cho.json", 'r') as f:
        cho_manifesto = json.load(f)
    cho_text = cho_manifesto['Seung Hui Cho']['Seung Hui Cho Manifesto']

    comment_words = ' '
    stopwords = set(STOPWORDS)

    tokens = cho_text.split()

    for i in range (len(tokens)):
        tokens[i] = tokens[i].lower()
    for words in tokens:
        comment_words = comment_words + words + ' '
    # print(comment_words)
    wordcloud = WordCloud(width = 800, height = 800,
                    background_color ='black',
                    stopwords = stopwords,
                    min_font_size = 10).generate(comment_words)
    # plot the WordCloud image
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud,  interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout(pad = 0)
    plt.show()


# Run functions here
# word_cloud_roof()
# word_cloud_rodger()
# word_cloud_cho()


# Functions

# I want to create a word cloud of each manifesto of most word used
    # Realted to that, I want to create a graph of each manifesto of most word used

# I want to create a graph of word count for each manifesto
    # Related to that, show which one has the most words, comparing each manifesto

# I want to show which one had the most unique vocabulary

# Perform sentiment analysis?
    # Negative or positive, although it will probaly be all negative
    # Will need time to read up on



# Some sites to consider:
# https://www.kaggle.com/ngyptr/python-nltk-sentiment-analysis
# https://www.digitalvidya.com/blog/an-introduction-to-text-analysis-in-python/
