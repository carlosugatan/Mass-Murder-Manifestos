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

with open("manifesto-data.json", 'r') as f:
    manifesto_data = json.load(f)

class Manifesto(object):
    def __init__(self, author, title, manifesto_data):
        self.manifesto_word_lst = []
        # self.author = ' '.join(manifesto_data[author].keys())
        self.author = author
        self.manifesto = manifesto_data[author][title]

        # cleaning data
        self.manifesto_clean = "".join((char for char in self.manifesto if char not in string.punctuation))
        self.tokens = self.manifesto_clean.split()
        for i in range (len(self.tokens)):
            self.tokens[i] = self.tokens[i].lower()
            self.manifesto_word_lst.append(self.tokens[i])

        # get rid of stopwords
        self.filtered_manifesto = [w for w in self.tokens if not w in stopwords]
        self.filtered_manifesto = [] ## No stopwords
        for w in self.tokens:
            if w not in stopwords:
                self.filtered_manifesto.append(w)

        # unique words
        self.unique_words_lst = []
        for word in self.manifesto_word_lst:
            if word not in self.unique_words_lst:
                self.unique_words_lst.append(word)
            else:
                pass

    def __str__(self):
        return '{}, {}'.format(self.author, self.manifesto)

    def word_lst(self): ## returns self.manifesto_word_lst to be used for specific data analysis (such as using pandas)
        return self.manifesto_word_lst

    ## returns unique words to be used for specific data analysis (such as using pandas)
    def unique_words(self):
        return self.unique_words_lst

    ## Word Cloud Function
    def word_cloud(self):
        comment_words = ' '
        for words in self.tokens:
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

    ## Vulgar Words Function
    def vulgar_words(self):
        vulgar_words = ' '
        for vulgar_word in vulgar_words_lst:
            if vulgar_word in self.filtered_manifesto:
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

    ## Sentiment Analysis functions ##
    def sentiment_analysis(self):
        sia = SIA()
        results = []

        for line in self.filtered_manifesto:
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

    ## Pronoun Functions ##
    def pronouns_analysis(self):
        pronouns = ' '
        for pronoun in pronouns_lst:
            if pronoun in self.manifesto_word_lst: ## not filtered
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


## Word Count Functions ##
## Please make sure manifesto variable names matches DataFrame. Sorry I couldn't figure out the best way to solve this right now.
def word_count():
    df=pd.DataFrame({'Authors': [ 'Adkisson', 'Auvinen', 'Cho', 'Dorner', 'Kaczynski', 'Rodger', 'Roof'],
                     'Number of Words': [len(adkisson.word_lst()),len(auvinen.word_lst()),len(cho.word_lst()),len(dorner.word_lst()),len(kaczynski.word_lst()),len(rodger.word_lst()),len(roof.word_lst())],})

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
    original = (len(adkisson.word_lst()),len(auvinen.word_lst()),len(cho.word_lst()),len(dorner.word_lst()),len(kaczynski.word_lst()),len(rodger.word_lst()),len(roof.word_lst()))
    unique_words = (len(adkisson.unique_words()),len(auvinen.unique_words()),len(cho.unique_words()),len(dorner.unique_words()),len(kaczynski.unique_words()),len(rodger.unique_words()),len(roof.unique_words()))

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


adkisson = Manifesto("Jim Adkisson", "The Adkisson Manifesto", manifesto_data)

auvinen = Manifesto("Eric Auvinen", "Natural Selector's Manifesto", manifesto_data)

cho = Manifesto("Seung Hui Cho", "Seung Hui Cho Manifesto", manifesto_data)

dorner = Manifesto("Christopher Dorner", "Christopher Dorner's Manifesto", manifesto_data)

kaczynski = Manifesto("Ted Kaczynski", "Industrial Society and Its Future", manifesto_data)

rodger = Manifesto("Elliot Rodger", "The Twisted World: The Story of Elliot Rodger", manifesto_data)

roof = Manifesto("Dylan Roof", "Dylan Roof Manifesto", manifesto_data)


## Functions

# dylan_roof.word_cloud()
# rodger.sentiment_analysis()
# rodger.word_cloud()
# chris_dorner.vulgar_words()
# print(rodger.word_lst())
# word_count()
# unique_words()
# print(roof.unique_words())
# roof.pronouns_analysis()
