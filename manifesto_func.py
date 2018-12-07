# import statements
import string
import numpy as np
import nltk
import json
from data_scraper import *
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

## Setting up manifesto_data to load text data
## Setting up each variable of each author of manifesto to their manifesto text
with open ("manifesto-data.json", 'r') as f:
    manifesto_data = json.load(f)

    ## Adkission
    adkission_text = manifesto_data['Adkission Manifesto']["The Adkission Manifesto"]
    adkission_text = "".join((char for char in adkission_text if char not in string.punctuation))
    tokens_adkission = adkission_text.split()
    adkission_word_lst = [] ## Total words
    for i in range (len(tokens_adkission)):
        tokens_adkission[i] = tokens_adkission[i].lower()
        adkission_word_lst.append(tokens_adkission[i])
    ## get rid of stopwords
    filtered_adkission = [w for w in tokens_adkission if not w in stopwords]
    filtered_adkission = [] ## No stopwords
    for w in tokens_adkission:
        if w not in stopwords:
            filtered_adkission.append(w)

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
    roof_text = manifesto_data['Dylan Roof']['Dylan Roof Manifesto']
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
def word_cloud_roof():
    comment_words = ' '
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

def word_cloud_adkission():
    comment_words = ' '

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
def vulgar_words_adkission():
    vulgar_words = ' '
    for vulgar_word in vulgar_words_lst:
        if vulgar_word in filtered_adkission:
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

    df=pd.DataFrame({'Authors': [ 'Adkission', 'Auvinen', 'Cho', 'Dorner', 'Kaczynski', 'Rodger', 'Roof'],
                     'Number of Words': [len(adkission_word_lst),len(auvinen_word_lst),len(cho_word_lst),len(dorner_word_lst),len(kaczynski_word_lst),len(rodger_word_lst),len(roof_word_lst)],})

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

    # Adkission
    adkission_words = []
    for word in adkission_word_lst:
        if word not in adkission_words:
            adkission_words.append(word)
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

    original = (len(adkission_word_lst),len(auvinen_word_lst),len(cho_word_lst),len(dorner_word_lst),len(kaczynski_word_lst),len(rodger_word_lst),len(roof_word_lst))
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

## Sentiment Analysis functions ##

def sentiment_adkission():
    sia = SIA()
    results = []

    for line in filtered_adkission:
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


# Some sites to consider:
# https://www.kaggle.com/ngyptr/python-nltk-sentiment-analysis
# https://www.digitalvidya.com/blog/an-introduction-to-text-analysis-in-python/
# https://www.cs.cmu.edu/~biglou/resources/
# https://stackoverflow.com/questions/23591254/python-pandas-matplotlib-annotating-labels-above-bar-chart-columns
# https://www.geeksforgeeks.org/removing-stop-words-nltk-python/
# https://www.learndatasci.com/tutorials/sentiment-analysis-reddit-headlines-pythons-nltk/
