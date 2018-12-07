# import statements
import json
from data_scraper import *
import numpy as np
# Python program to generate WordCloud
from wordcloud import WordCloud, STOPWORDS
# import matplotlib as mpl
# mpl.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd

# pip install matplotlib
# conda install matplotlib
# pip install pandas
# conda install pandas
# pip install wordcloud

# maybe: conda install scipy
# pip freeze > requirements.txt

## Vulgar Words List
vulgar_words_lst = []
with open('vulgar_words.txt', mode='r') as f:
    contents_vulgar_words = f.readlines()
    for words in contents_vulgar_words:
        words = words.replace('\n', '')
        vulgar_words_lst.append(words)

## Setting up stopwords
stopwords = set(STOPWORDS)

## Setting up manifesto_data to load text data
## Setting up each variable of each author of manifesto to their manifesto text
with open ("manifesto-data.json", 'r') as f:
    manifesto_data = json.load(f)

    ## Adkission
    adkission_text = manifesto_data['Adkission Manifesto']["The Adkission Manifesto"]
    tokens_adkission = adkission_text.split()

    ## Auvinen
    auvinen_text = manifesto_data['Eric Auvinen']["Natural Selector's Manifesto"]
    tokens_auvinen = auvinen_text.split()

    ## Dorner
    dorner_text = manifesto_data['Christopher Dorner']["Christopher Dorner's Manifesto"]
    tokens_dorner = dorner_text.split()

    ## Cho
    cho_text = manifesto_data['Seung Hui Cho']['Seung Hui Cho Manifesto']
    tokens_cho = cho_text.split()
    cho_word_lst = []
    for i in range (len(tokens_cho)):
        tokens_cho[i] = tokens_cho[i].lower()
        cho_word_lst.append(tokens_cho[i])

    ## Kaczynski
    kaczynski_text = manifesto_data['Ted Kaczynski']["Industrial Society and Its Future"]
    tokens_kaczynski = kaczynski_text.split()

    ## Rodger
    rodger_text = manifesto_data['Elliot Rodger']['The Twisted World: The Story of Elliot Rodger']
    tokens_rodger = rodger_text.split()

    ## Roof
    roof_text = manifesto_data['Dylan Roof']['Dylan Roof Manifesto']
    tokens_roof = roof_text.split()


## Word Cloud Functions ##
def word_cloud_roof():
    comment_words = ' '

    for i in range (len(tokens_roof)):
        tokens_roof[i] = tokens_roof[i].lower()
    for words in tokens_roof:
        comment_words = comment_words + words + ' '

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
    comment_words = ' '

    for i in range (len(tokens_rodger)):
        tokens_rodger[i] = tokens_rodger[i].lower()
    for words in tokens_rodger:
        comment_words = comment_words + words + ' '

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
    comment_words = ' '

    for i in range (len(tokens_cho)):
        tokens_cho[i] = tokens_cho[i].lower()
    for words in tokens_cho:
        comment_words = comment_words + words + ' '

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

def word_cloud_auvinen():
    comment_words = ' '

    tokens_auvinen = auvinen_text.split()

    for i in range (len(tokens_auvinen)):
        tokens_auvinen[i] = tokens_auvinen[i].lower()
    for words in tokens_auvinen:
        comment_words = comment_words + words + ' '

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

def word_cloud_kaczynski():
    comment_words = ' '

    for i in range (len(tokens_kaczynski)):
        tokens_kaczynski[i] = tokens_kaczynski[i].lower()
    for words in tokens_kaczynski:
        comment_words = comment_words + words + ' '

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

def word_cloud_dorner():
    comment_words = ' '

    for i in range (len(tokens_dorner)):
        tokens_dorner[i] = tokens_dorner[i].lower()
    for words in tokens_dorner:
        comment_words = comment_words + words + ' '

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

def word_cloud_adkission():
    comment_words = ' '

    for i in range (len(tokens_adkission)):
        tokens_adkission[i] = tokens_adkission[i].lower()
    for words in tokens_adkission:
        comment_words = comment_words + words + ' '

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

## Vulgar Words Functions ##
def vulgar_words_roof():
    roof_word_lst = []
    with open ("manifesto-data.json", 'r') as f:
        roof_manifesto = json.load(f)
    roof_text = roof_manifesto['Dylan Roof']['Dylan Roof Manifesto']
    tokens = roof_text.split()

    for i in range (len(tokens)):
        tokens[i] = tokens[i].lower()
        roof_word_lst.append(tokens[i])

    for vulgar_word in vulgar_words_lst:
        if vulgar_word in roof_word_lst:
            print(vulgar_word)


def vulgar_words_rodger():
    rodger_word_lst = []
    with open ("manifesto-data.json", 'r') as f:
        rodger_manifesto = json.load(f)
    rodger_text = rodger_manifesto['Elliot Rodger']['The Twisted World: The Story of Elliot Rodger']
    tokens = rodger_text.split()

    for i in range (len(tokens)):
        tokens[i] = tokens[i].lower()
        rodger_word_lst.append(tokens[i])

    for vulgar_word in vulgar_words_lst:
        if vulgar_word in rodger_word_lst:
            print(vulgar_word)

def vulgar_words_cho():
    cho_word_lst = []
    with open ("manifesto-data.json", 'r') as f:
        cho_manifesto = json.load(f)
    cho_text = cho_manifesto['Seung Hui Cho']['Seung Hui Cho Manifesto']
    tokens = cho_text.split()

    for i in range (len(tokens)):
        tokens[i] = tokens[i].lower()
        cho_word_lst.append(tokens[i])

    for vulgar_word in vulgar_words_lst:
        if vulgar_word in cho_word_lst:
            print(vulgar_word)


### WORD CLOUD FOR VULGAR WORDS ###
def word_cloud_fuck():
    cho_word_lst = []
    with open ("manifesto-data.json", 'r') as f:
        cho_manifesto = json.load(f)
    cho_text = cho_manifesto['Seung Hui Cho']['Seung Hui Cho Manifesto']
    vulgar_words = ' '
    tokens = cho_text.split()

    for i in range (len(tokens)):
        tokens[i] = tokens[i].lower()
        cho_word_lst.append(tokens[i])

    for vulgar_word in vulgar_words_lst:
        if vulgar_word in cho_word_lst:
            vulgar_words = vulgar_words + vulgar_word + ' '

    wordcloud = WordCloud(width = 800, height = 800,
                    background_color ='black',
                    min_font_size = 10).generate(vulgar_words)
    # plot the WordCloud image
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud,  interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout(pad = 0)
    plt.show()

## Word Count Functions ##
def word_count():

    df=pd.DataFrame({'Authors': [ 'Adkission', 'Auvinen', 'Cho', 'Dorner', 'Kaczynski', 'Rodger', 'Roof'],
                     'Number of Words': [len(tokens_adkission),len(tokens_auvinen),len(tokens_cho),len(tokens_dorner),len(tokens_kaczynski),len(tokens_rodger),len(tokens_roof)],})

    df = df.set_index('Authors')
    ax = df.plot(kind='bar',  title='Total Words in Manifesto')
    ax.set_ylabel('Number of Words')
    ax.set_ylim(0, 130000)
    for i, label in enumerate(list(df.index)):
        score = df.ix[label]['Number of Words']
        ax.annotate(str(score), (i-0.299, score + 0.04), fontsize=9)
    plt.tight_layout(pad = 1)
    plt.show()

def unique_words():

    # Cho
    cho_words = []
    for word in tokens_cho:
        if word not in cho_words:
            cho_words.append(word)
        else:
            pass

    # Rodger
    rodger_words = []
    for word in tokens_rodger:
        if word not in rodger_words:
            rodger_words.append(word)
        else:
            pass

    # Adkission
    adkission_words = []
    for word in tokens_adkission:
        if word not in adkission_words:
            adkission_words.append(word)
        else:
            pass

    # Auvinen
    auvinen_words = []
    for word in tokens_auvinen:
        if word not in auvinen_words:
            auvinen_words.append(word)
        else:
            pass

    # Dorner
    dorner_words = []
    for word in tokens_dorner:
        if word not in dorner_words:
            dorner_words.append(word)
        else:
            pass

    # Kaczynski
    kaczynski_words = []
    for word in tokens_kaczynski:
        if word not in kaczynski_words:
            kaczynski_words.append(word)
        else:
            pass

    # Roof
    roof_words = []
    for word in tokens_roof:
        if word not in roof_words:
            roof_words.append(word)
        else:
            pass

    original = (len(tokens_adkission),len(tokens_auvinen),len(tokens_cho),len(tokens_dorner),len(tokens_kaczynski),len(tokens_rodger),len(tokens_roof))
    unique_words = (len(adkission_words),len(auvinen_words),len(cho_words),len(dorner_words),len(kaczynski_words),len(rodger_words),len(roof_words))

    ind = np.arange(len(original))  # the x locations for the groups
    width = 0.43  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind - width/2, original, width,
                    color='SkyBlue', label='Original')
    rects2 = ax.bar(ind + width/2, unique_words, width,
                    color='IndianRed', label='Unique Words')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Number of Words')
    ax.set_title('Orignal text vs. unique words')
    ax.set_xticks(ind)
    ax.set_xticklabels(('Adkission', 'Auvinen', 'Cho', 'Dorner', 'Kaczynski', 'Rodger', 'Roof'))
    ax.legend()

    def autolabel(rects, xpos='center'):
        xpos = xpos.lower()  # normalize the case of the parameter
        ha = {'center': 'center', 'right': 'left', 'left': 'right'}
        offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                    '{}'.format(height), ha=ha[xpos], va='bottom', fontsize=6.5)

    autolabel(rects1)
    autolabel(rects2)
    plt.tight_layout(pad = 1)
    plt.show()

### %%%% RUN FUNCTIONS HERE %%%% ###

# unique_words()

# word_count()

## Vulgar words functions ##
# vulgar_words_roof()
# vulgar_words_rodger()
# vulgar_words_cho()
# word_cloud_fuck()

## Word cloud functions ##
# word_cloud_roof()
# word_cloud_rodger()
# word_cloud_cho()
# word_cloud_auvinen()
# word_cloud_kaczynski()
# word_cloud_dorner()
# word_cloud_adkission()

# Functions

# I want to create a word cloud of each manifesto of most word used - DONE
    # Realted to that, I want to create a graph of each manifesto of most word used

# I want to create a graph of word count for each manifesto - DONE
    # Related to that, show which one has the most words, comparing each manifesto - DONE

# I want to show which one had the most unique vocabulary - DONE

# Perform sentiment analysis?
    # Negative or positive, although it will probaly be all negative
    # Will need time to read up on



# Some sites to consider:
# https://www.kaggle.com/ngyptr/python-nltk-sentiment-analysis
# https://www.digitalvidya.com/blog/an-introduction-to-text-analysis-in-python/
# https://www.cs.cmu.edu/~biglou/resources/
# https://stackoverflow.com/questions/23591254/python-pandas-matplotlib-annotating-labels-above-bar-chart-columns
