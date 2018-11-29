## Carlo Sugatan
## SI 508 Final Project

# import statements
import json
from bs4 import BeautifulSoup
from improved_cache_v1 import *
import requests
import textract
from datetime import datetime

# Textract
# Dylan Roof
dylan_roof = textract.process("/Users/Carlo/Google Drive/FA18 Classes/SI508/Assignments - HW/Final Project/Manifesto-Project/Dylan_Roof.pdf", encoding='utf_8')

manifesto_dict = {}

manifesto_dict['Dylan Roof'] = {}
manifesto_dict['Dylan Roof']['Dylan Roof Manifesto'] = dylan_roof

print(manifesto_dict)
# Elliot Rodger
# elliot_rodger = textract.process("/Users/Carlo/Google Drive/FA18 Classes/SI508/Assignments - HW/Final Project/Manifesto-Project/Elliot_Rodger.pdf", encoding='utf_8')

#Seung Hui Cho
# seung_hui_cho = textract.process("/Users/Carlo/Google Drive/FA18 Classes/SI508/Assignments - HW/Final Project/Manifesto-Project/seung_hui_cho.pdf", encoding='utf_8')

# Anders Breivik
# anders_breivik = textract.process("/Users/Carlo/Google Drive/FA18 Classes/SI508/Assignments - HW/Final Project/Manifesto-Project/Anders_Behring_Breivik.pdf", encoding='utf_8')

# Eric Auvinen
# eric_auvinen = textract.process("/Users/Carlo/Google Drive/FA18 Classes/SI508/Assignments - HW/Final Project/Manifesto-Project/Auvinen.doc", encoding='utf_8')

# Ted Kaczynski
# ted_kaczynski = textract.process("/Users/Carlo/Google Drive/FA18 Classes/SI508/Assignments - HW/Final Project/Manifesto-Project/Ted_Kaczynski.pdf", encoding='utf_8')
# print(ted_kaczynski)

# Web Scraping
CACHE_FNAME = "manifesto-data.json"

# Christopher Dorner
# url_to_scrape = "http://www.laist.com/2013/02/07/christopher_dorners_manifesto_in_fu.php"
# manifesto_text = soup.find('blockquote').text
# print(manifesto_text)

# Adkission Manifesto
# url_to_scrape = "https://faith17983.wordpress.com/2015/05/31/the-adkisson-manifesto/"
# manifesto_text = soup.find('div', class_ = 'entry-content')
# manifesto_text = manifesto_text.text

# primary_cache = Cache(CACHE_FNAME)
#
# while primary_cache.get(url_to_scrape) is None:
# 	data = requests.get(url_to_scrape)
# 	html_text = data.text
# 	primary_cache.set(url_to_scrape,html_text)
#
# soup = BeautifulSoup(primary_cache.get(url_to_scrape), features="html.parser")
# # page_title = soup.title.text
# # print(page_title)
# manifesto_text = soup.find('div', class_ = 'entry-content')
# manifesto_text = manifesto_text.text
# # manifesto_text = soup.find_all('td')
# print(manifesto_text)

# print(soup.find("a")) # For example




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
