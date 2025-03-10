# import statements
import string
import numpy as np
import nltk
import json
# from data_scraper import *
import numpy as np
# Python program to generate WordCloud
from wordcloud import WordCloud, STOPWORDS
# import matplotlib as mpl
# mpl.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

# pip install matplotlib
# conda install matplotlib
# pip install pandas
# conda install pandas
# pip install wordcloud
# sudo pip install -U nltk
# >> import nltk
# >> nltk.download('vader_lexicon')

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

## Pronouns List
pronouns_lst = []
with open('pronouns.txt', mode='r') as f:
    contents_pronoun_words = f.readlines()
    for words in contents_pronoun_words:
        words = words.replace('\n', '')
        pronouns_lst.append(words)

## Setting up manifesto_data to load text data
## Setting up each variable of each author of manifesto to their manifesto text
with open ("manifesto-data.json", 'r') as f:
    manifesto_data = json.load(f)

    ## adkisson
    adkisson_text = manifesto_data['Jim Adkisson']["The Adkisson Manifesto"]
    # remove punctuations: https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
    adkisson_text = "".join((char for char in adkisson_text if char not in string.punctuation))
    # split each word
    tokens_adkisson = adkisson_text.split()
    adkisson_word_lst = [] ## Total words
    for i in range (len(tokens_adkisson)):
        tokens_adkisson[i] = tokens_adkisson[i].lower()
        adkisson_word_lst.append(tokens_adkisson[i])
    ## get rid of stopwords
    # https://www.geeksforgeeks.org/removing-stop-words-nltk-python/
    filtered_adkisson = [w for w in tokens_adkisson if not w in stopwords]
    filtered_adkisson = [] ## No stopwords
    for w in tokens_adkisson:
        if w not in stopwords:
            filtered_adkisson.append(w)

    ## Auvinen
    auvinen_text = manifesto_data['Eric Auvinen']["Natural Selector's Manifesto"]
    auvinen_text = "".join((char for char in auvinen_text if char not in string.punctuation))
    tokens_auvinen = auvinen_text.split()
    auvinen_word_lst = [] ## Total words
    for i in range (len(tokens_auvinen)):
        tokens_auvinen[i] = tokens_auvinen[i].lower()
        auvinen_word_lst.append(tokens_auvinen[i])
    ## get rid of stopwords
    filtered_auvinen = [w for w in tokens_auvinen if not w in stopwords]
    filtered_auvinen = [] ## No stopwords
    for w in tokens_auvinen:
        if w not in stopwords:
            filtered_auvinen.append(w)

    ## Dorner
    dorner_text = manifesto_data['Christopher Dorner']["Christopher Dorner's Manifesto"]
    dorner_text = "".join((char for char in dorner_text if char not in string.punctuation))
    tokens_dorner = dorner_text.split()
    dorner_word_lst = [] ## Total words
    for i in range (len(tokens_dorner)):
        tokens_dorner[i] = tokens_dorner[i].lower()
        dorner_word_lst.append(tokens_dorner[i])
    ## get rid of stopwords
    filtered_dorner = [w for w in tokens_dorner if not w in stopwords]
    filtered_dorner = [] ## No stopwords
    for w in tokens_dorner:
        if w not in stopwords:
            filtered_dorner.append(w)

    ## Cho
    cho_text = manifesto_data['Seung Hui Cho']['Seung Hui Cho Manifesto']
    cho_text = "".join((char for char in cho_text if char not in string.punctuation))
    tokens_cho = cho_text.split()
    cho_word_lst = []
    for i in range (len(tokens_cho)):
        tokens_cho[i] = tokens_cho[i].lower()
        cho_word_lst.append(tokens_cho[i])
    ## get rid of stopwords
    filtered_cho = [w for w in tokens_cho if not w in stopwords]
    filtered_cho = [] ## No stopwords
    for w in tokens_cho:
        if w not in stopwords:
            filtered_cho.append(w)

    ## Kaczynski
    kaczynski_text = manifesto_data['Ted Kaczynski']["Industrial Society and Its Future"]
    kaczynski_text = "".join((char for char in kaczynski_text if char not in string.punctuation))
    tokens_kaczynski = kaczynski_text.split()
    kaczynski_word_lst = []
    for i in range (len(tokens_kaczynski)):
        tokens_kaczynski[i] = tokens_kaczynski[i].lower()
        kaczynski_word_lst.append(tokens_kaczynski[i])
    ## get rid of stopwords
    filtered_kaczynski = [w for w in tokens_kaczynski if not w in stopwords]
    filtered_kaczynski = [] ## No stopwords
    for w in tokens_kaczynski:
        if w not in stopwords:
            filtered_kaczynski.append(w)

    ## Rodger
    rodger_text = manifesto_data['Elliot Rodger']['The Twisted World: The Story of Elliot Rodger']
    rodger_text = "".join((char for char in rodger_text if char not in string.punctuation))
    tokens_rodger = rodger_text.split()
    rodger_word_lst = []
    for i in range (len(tokens_rodger)):
        tokens_rodger[i] = tokens_rodger[i].lower()
        rodger_word_lst.append(tokens_rodger[i])
    ## get rid of stopwords
    filtered_rodger = [w for w in tokens_rodger if not w in stopwords]
    filtered_rodger = [] ## No stopwords
    for w in tokens_rodger:
        if w not in stopwords:
            filtered_rodger.append(w)

    ## Roof
    roof_text = manifesto_data['Dylann Roof']['Dylann Roof Manifesto']
    roof_text = "".join((char for char in roof_text if char not in string.punctuation))
    tokens_roof = roof_text.split()
    roof_word_lst = []
    for i in range (len(tokens_roof)):
        tokens_roof[i] = tokens_roof[i].lower()
        roof_word_lst.append(tokens_roof[i])
    ## get rid of stopwords
    filtered_roof = [w for w in tokens_roof if not w in stopwords]
    filtered_roof = [] ## No stopwords
    for w in tokens_roof:
        if w not in stopwords:
            filtered_roof.append(w)

## Word Cloud Functions ##
## documentation from https://amueller.github.io/word_cloud/
def word_cloud_roof():
    comment_words = ' '
    for words in tokens_roof: # reads each word
        comment_words = comment_words + words + ' ' # accumulate each word

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

def word_cloud_adkisson():
    comment_words = ' '

    for words in tokens_adkisson:
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
def vulgar_words_adkisson():
    vulgar_words = ' '
    for vulgar_word in vulgar_words_lst:
        if vulgar_word in filtered_adkisson:
            vulgar_words = vulgar_words + vulgar_word + ' '   # accumulate each word

    wordcloud = WordCloud(width = 800, height = 800,
                    background_color ='black',
                    min_font_size = 10).generate(vulgar_words)
    # plot the WordCloud image
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud,  interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout(pad = 0)
    plt.show()

def vulgar_words_auvinen():
    vulgar_words = ' '
    for vulgar_word in vulgar_words_lst:
        if vulgar_word in filtered_auvinen:
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

def vulgar_words_cho():
    vulgar_words = ' '
    for vulgar_word in vulgar_words_lst:
        if vulgar_word in filtered_cho:
            print(vulgar_word)
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

def vulgar_words_dorner():
    vulgar_words = ' '
    for vulgar_word in vulgar_words_lst:
        if vulgar_word in filtered_dorner:
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

def vulgar_words_kaczynski():
    vulgar_words = ' '
    for vulgar_word in vulgar_words_lst:
        if vulgar_word in filtered_kaczynski:
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

def vulgar_words_rodger():
    vulgar_words = ' '
    for vulgar_word in vulgar_words_lst:
        if vulgar_word in filtered_rodger:
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

def vulgar_words_roof():
    vulgar_words = ' '
    for vulgar_word in vulgar_words_lst:
        if vulgar_word in filtered_roof:
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
## Pandas documentation and sample charts
# https://stackoverflow.com/questions/23591254/python-pandas-matplotlib-annotating-labels-above-bar-chart-columns

## data frame for authors and number of words respectively
    df=pd.DataFrame({'Authors': [ 'Adkisson', 'Auvinen', 'Cho', 'Dorner', 'Kaczynski', 'Rodger', 'Roof'],
                     'Number of Words': [len(adkisson_word_lst),len(auvinen_word_lst),len(cho_word_lst),len(dorner_word_lst),len(kaczynski_word_lst),len(rodger_word_lst),len(roof_word_lst)],})

    df = df.set_index('Authors')
    ax = df.plot(kind='bar',  title='Total Words in Manifesto')
    ax.set_ylabel('Number of Words')
    ax.set_ylim(0, 130000) # charting so things don't look funky
    for i, label in enumerate(list(df.index)):
        score = df.ix[label]['Number of Words']
        ax.annotate(str(score), (i-0.299, score + 0.04), fontsize=9)
    plt.tight_layout(pad = 1)
    plt.show()

def unique_words():
## matplotlib documentation and sample charts

    # Cho
    cho_words = []
    for word in cho_word_lst:
        if word not in cho_words:
            cho_words.append(word)
        else:
            pass

    # Rodger
    rodger_words = []
    for word in rodger_word_lst:
        if word not in rodger_words:
            rodger_words.append(word)
        else:
            pass

    # Adkisson
    adkisson_words = []
    for word in adkisson_word_lst:
        if word not in adkisson_words:
            adkisson_words.append(word)
        else:
            pass

    # Auvinen
    auvinen_words = []
    for word in auvinen_word_lst:
        if word not in auvinen_words:
            auvinen_words.append(word)
        else:
            pass

    # Dorner
    dorner_words = []
    for word in dorner_word_lst:
        if word not in dorner_words:
            dorner_words.append(word)
        else:
            pass

    # Kaczynski
    kaczynski_words = []
    for word in kaczynski_word_lst:
        if word not in kaczynski_words:
            kaczynski_words.append(word)
        else:
            pass

    # Roof
    roof_words = []
    for word in roof_word_lst:
        if word not in roof_words:
            roof_words.append(word)
        else:
            pass

    original = (len(adkisson_word_lst),len(auvinen_word_lst),len(cho_word_lst),len(dorner_word_lst),len(kaczynski_word_lst),len(rodger_word_lst),len(roof_word_lst))
    unique_words = (len(adkisson_words),len(auvinen_words),len(cho_words),len(dorner_words),len(kaczynski_words),len(rodger_words),len(roof_words))

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
    ax.set_xticklabels(('Adkisson', 'Auvinen', 'Cho', 'Dorner', 'Kaczynski', 'Rodger', 'Roof'))
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

## Sentiment Analysis functions ##
#https://github.com/LearnDataSci/article-resources/blob/master/Sentiment%20Analysis%20on%20Reddit%20Headlines%20with%20NLTK/Sentiment%20Analysis%20on%20Reddit%20Headlines%20with%20NLTK.ipynb
# # https://www.kaggle.com/ngyptr/python-nltk-sentiment-analysis
# https://www.learndatasci.com/tutorials/sentiment-analysis-reddit-headlines-pythons-nltk/
def sentiment_adkisson():
    sia = SIA()
    results = []
    # calculating polarity score of each word
    for line in filtered_adkisson: # no stopwords
        pol_score = sia.polarity_scores(line)
        pol_score['word'] = line
        results.append(pol_score)
    # put into a dataframe
    df = pd.DataFrame.from_records(results)
    df.head()
    # for plotting
    df['label'] = 0
    df.loc[df['compound'] > 0.2, 'label'] = 1
    df.loc[df['compound'] < -0.2, 'label'] = -1
    df.head()

    df.label.value_counts(normalize=True) * 100

    fig, ax = plt.subplots(figsize=(8, 8))

    counts = df.label.value_counts(normalize=True) * 100

    x = counts.index
    y = counts
    ax.set_ylabel('Percentage')
    ax.set_title('Sentiment Analysis of Adkisson ')
    rects = plt.bar(x, y)
    plt.xticks(x, ("Neutral", "Negative", "Positive"))


    def autolabel(rects, xpos='center'):
        xpos = xpos.lower()  # normalize the case of the parameter
        ha = {'center': 'center', 'right': 'left', 'left': 'right'}
        offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                    '{}'.format(height), ha=ha[xpos], va='bottom', fontsize=9)

    autolabel(rects)
    plt.tight_layout(pad = 1)
    plt.show()

def sentiment_auvinen():
    sia = SIA()
    results = []

    for line in filtered_auvinen:
        pol_score = sia.polarity_scores(line)
        pol_score['word'] = line
        results.append(pol_score)

    df = pd.DataFrame.from_records(results)
    df.head()

    df['label'] = 0
    df.loc[df['compound'] > 0.2, 'label'] = 1
    df.loc[df['compound'] < -0.2, 'label'] = -1
    df.head()

    df.label.value_counts(normalize=True) * 100

    fig, ax = plt.subplots(figsize=(8, 8))

    counts = df.label.value_counts(normalize=True) * 100

    x = counts.index
    y = counts
    ax.set_ylabel('Percentage')
    ax.set_title('Sentiment Analysis')
    rects = plt.bar(x, y)
    plt.xticks(x, ("Neutral", "Negative", "Positive"))


    def autolabel(rects, xpos='center'):
        xpos = xpos.lower()  # normalize the case of the parameter
        ha = {'center': 'center', 'right': 'left', 'left': 'right'}
        offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                    '{}'.format(height), ha=ha[xpos], va='bottom', fontsize=9)

    autolabel(rects)
    plt.tight_layout(pad = 1)
    plt.show()

def sentiment_cho():
    sia = SIA()
    results = []

    for line in filtered_cho:
        pol_score = sia.polarity_scores(line)
        pol_score['word'] = line
        results.append(pol_score)

    df = pd.DataFrame.from_records(results)
    df.head()

    df['label'] = 0
    df.loc[df['compound'] > 0.2, 'label'] = 1
    df.loc[df['compound'] < -0.2, 'label'] = -1
    df.head()

    df.label.value_counts(normalize=True) * 100

    fig, ax = plt.subplots(figsize=(8, 8))

    counts = df.label.value_counts(normalize=True) * 100

    x = counts.index
    y = counts
    ax.set_ylabel('Percentage')
    ax.set_title('Sentiment Analysis')
    rects = plt.bar(x, y)
    plt.xticks(x, ("Neutral", "Negative", "Positive"))


    def autolabel(rects, xpos='center'):
        xpos = xpos.lower()  # normalize the case of the parameter
        ha = {'center': 'center', 'right': 'left', 'left': 'right'}
        offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                    '{}'.format(height), ha=ha[xpos], va='bottom', fontsize=9)

    autolabel(rects)
    plt.tight_layout(pad = 1)
    plt.show()

def sentiment_dorner():
    sia = SIA()
    results = []

    for line in filtered_dorner:
        pol_score = sia.polarity_scores(line)
        pol_score['word'] = line
        results.append(pol_score)

    df = pd.DataFrame.from_records(results)
    df.head()

    df['label'] = 0
    df.loc[df['compound'] > 0.2, 'label'] = 1
    df.loc[df['compound'] < -0.2, 'label'] = -1
    df.head()

    df.label.value_counts(normalize=True) * 100

    fig, ax = plt.subplots(figsize=(8, 8))

    counts = df.label.value_counts(normalize=True) * 100

    x = counts.index
    y = counts
    ax.set_ylabel('Percentage')
    ax.set_title('Sentiment Analysis')
    rects = plt.bar(x, y)
    plt.xticks(x, ("Neutral", "Negative", "Positive"))


    def autolabel(rects, xpos='center'):
        xpos = xpos.lower()  # normalize the case of the parameter
        ha = {'center': 'center', 'right': 'left', 'left': 'right'}
        offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                    '{}'.format(height), ha=ha[xpos], va='bottom', fontsize=9)

    autolabel(rects)
    plt.tight_layout(pad = 1)
    plt.show()

def sentiment_kaczynski():
    sia = SIA()
    results = []

    for line in filtered_kaczynski:
        pol_score = sia.polarity_scores(line)
        pol_score['word'] = line
        results.append(pol_score)

    df = pd.DataFrame.from_records(results)
    df.head()

    df['label'] = 0
    df.loc[df['compound'] > 0.2, 'label'] = 1
    df.loc[df['compound'] < -0.2, 'label'] = -1
    df.head()

    df.label.value_counts(normalize=True) * 100

    fig, ax = plt.subplots(figsize=(8, 8))

    counts = df.label.value_counts(normalize=True) * 100

    x = counts.index
    y = counts
    ax.set_ylabel('Percentage')
    ax.set_title('Sentiment Analysis')
    rects = plt.bar(x, y)
    plt.xticks(x, ("Neutral", "Negative", "Positive"))


    def autolabel(rects, xpos='center'):
        xpos = xpos.lower()  # normalize the case of the parameter
        ha = {'center': 'center', 'right': 'left', 'left': 'right'}
        offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                    '{}'.format(height), ha=ha[xpos], va='bottom', fontsize=9)

    autolabel(rects)
    plt.tight_layout(pad = 1)
    plt.show()


def sentiment_rodger():
    sia = SIA()
    results = []

    for line in filtered_rodger:
        pol_score = sia.polarity_scores(line)
        pol_score['word'] = line
        results.append(pol_score)

    df = pd.DataFrame.from_records(results)
    df.head()

    df['label'] = 0
    df.loc[df['compound'] > 0.2, 'label'] = 1
    df.loc[df['compound'] < -0.2, 'label'] = -1
    df.head()

    df.label.value_counts(normalize=True) * 100

    fig, ax = plt.subplots(figsize=(8, 8))

    counts = df.label.value_counts(normalize=True) * 100

    x = counts.index
    y = counts
    ax.set_ylabel('Percentage')
    ax.set_title('Sentiment Analysis')
    rects = plt.bar(x, y)
    plt.xticks(x, ("Neutral", "Negative", "Positive"))


    def autolabel(rects, xpos='center'):
        xpos = xpos.lower()  # normalize the case of the parameter
        ha = {'center': 'center', 'right': 'left', 'left': 'right'}
        offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                    '{}'.format(height), ha=ha[xpos], va='bottom', fontsize=9)

    autolabel(rects)
    plt.tight_layout(pad = 1)
    plt.show()

def sentiment_roof():
    sia = SIA()
    results = []

    for line in filtered_roof:
        pol_score = sia.polarity_scores(line)
        pol_score['word'] = line
        results.append(pol_score)

    df = pd.DataFrame.from_records(results)
    df.head()

    df['label'] = 0
    df.loc[df['compound'] > 0.2, 'label'] = 1
    df.loc[df['compound'] < -0.2, 'label'] = -1
    df.head()

    df.label.value_counts(normalize=True) * 100

    fig, ax = plt.subplots(figsize=(8, 8))

    counts = df.label.value_counts(normalize=True) * 100

    x = counts.index
    y = counts
    ax.set_ylabel('Percentage')
    ax.set_title('Sentiment Analysis of Dylann Roof Manifesto')
    rects = plt.bar(x, y)
    plt.xticks(x, ("Neutral", "Negative", "Positive"))


    def autolabel(rects, xpos='center'):
        xpos = xpos.lower()  # normalize the case of the parameter
        ha = {'center': 'center', 'right': 'left', 'left': 'right'}
        offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                    '{}'.format(height), ha=ha[xpos], va='bottom', fontsize=9)

    autolabel(rects)
    plt.tight_layout(pad = 1)
    plt.show()

## Pronoun Functions ##
def pronouns_adkisson():
    pronouns = ' '
    for pronoun in pronouns_lst:
        if pronoun in adkisson_word_lst: ## not filtered
            pronouns = pronouns + pronoun + ' '

    wordcloud = WordCloud(width = 800, height = 800,
                    background_color ='black',
                    min_font_size = 10).generate(pronouns)
    # plot the WordCloud image
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud,  interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout(pad = 0)
    plt.show()

def pronouns_auvinen():
    pronouns = ' '
    for pronoun in pronouns_lst:
        if pronoun in auvinen_word_lst: ## not filtered
            pronouns = pronouns + pronoun + ' '

    wordcloud = WordCloud(width = 800, height = 800,
                    background_color ='black',
                    min_font_size = 10).generate(pronouns)
    # plot the WordCloud image
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud,  interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout(pad = 0)
    plt.show()

def pronouns_cho():
    pronouns = ' '
    for pronoun in pronouns_lst:
        if pronoun in cho_word_lst: ## not filtered
            pronouns = pronouns + pronoun + ' '

    wordcloud = WordCloud(width = 800, height = 800,
                    background_color ='black',
                    min_font_size = 10).generate(pronouns)
    # plot the WordCloud image
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud,  interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout(pad = 0)
    plt.show()

def pronouns_dorner():
    pronouns = ' '
    for pronoun in pronouns_lst:
        if pronoun in dorner_word_lst: ## not filtered
            pronouns = pronouns + pronoun + ' '

    wordcloud = WordCloud(width = 800, height = 800,
                    background_color ='black',
                    min_font_size = 10).generate(pronouns)
    # plot the WordCloud image
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud,  interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout(pad = 0)
    plt.show()

def pronouns_kaczynski():
    pronouns = ' '
    for pronoun in pronouns_lst:
        if pronoun in kaczynski_word_lst: ## not filtered
            pronouns = pronouns + pronoun + ' '

    wordcloud = WordCloud(width = 800, height = 800,
                    background_color ='black',
                    min_font_size = 10).generate(pronouns)
    # plot the WordCloud image
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud,  interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout(pad = 0)
    plt.show()

def pronouns_rodger():
    pronouns = ' '
    for pronoun in pronouns_lst:
        if pronoun in rodger_word_lst: ## not filtered
            pronouns = pronouns + pronoun + ' '

    wordcloud = WordCloud(width = 800, height = 800,
                    background_color ='black',
                    min_font_size = 10).generate(pronouns)
    # plot the WordCloud image
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud,  interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout(pad = 0)
    # print(pronouns_lst)
    plt.show()

def pronouns_roof():
    pronouns = ' '
    for pronoun in pronouns_lst:
        if pronoun in roof_word_lst: ## not filtered
            pronouns = pronouns + pronoun + ' '

    wordcloud = WordCloud(width = 800, height = 800,
                    background_color ='black',
                    min_font_size = 10).generate(pronouns)
    # plot the WordCloud image
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud,  interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout(pad = 0)
    plt.show()


### %%%% RUN FUNCTIONS HERE %%%% ###

## Word Cloud Functions ##
# word_cloud_adkisson()
# word_cloud_auvinen()
# word_cloud_cho()
# word_cloud_dorner()
# word_cloud_kaczynski()
# word_cloud_roger()
# word_cloud_roof()

## Vulgar words functions ##
# vulgar_words_adkisson()
# vulgar_words_auvinen()
# vulgar_words_cho()
# vulgar_words_dorner()
# vulgar_words_kaczynski()
# vulgar_words_rodger()
# vulgar_words_roof()

## Pronouns Analysis functions ##
# pronouns_adkisson()
# pronouns_auvinen()
# pronouns_cho()
# pronouns_dorner()
# pronouns_kaczynski()
# pronouns_rodger()
# pronouns_roof()

## Sentiment Analysis Functions ##
# sentiment_adkisson()
# sentiment_auvinen()
# sentiment_cho()
# sentiment_dorner()
# sentiment_kaczynski()
# sentiment_rodger()
# sentiment_roof()

# word_count()

# unique_words()








# Somes sites used as references for project:
# https://www.kaggle.com/ngyptr/python-nltk-sentiment-analysis
# https://www.digitalvidya.com/blog/an-introduction-to-text-analysis-in-python/
# https://www.cs.cmu.edu/~biglou/resources/
# https://stackoverflow.com/questions/23591254/python-pandas-matplotlib-annotating-labels-above-bar-chart-columns
# https://www.geeksforgeeks.org/removing-stop-words-nltk-python/
# https://www.learndatasci.com/tutorials/sentiment-analysis-reddit-headlines-pythons-nltk/
# https://github.com/LearnDataSci/article-resources/blob/master/Sentiment%20Analysis%20on%20Reddit%20Headlines%20with%20NLTK/Sentiment%20Analysis%20on%20Reddit%20Headlines%20with%20NLTK.ipynb
