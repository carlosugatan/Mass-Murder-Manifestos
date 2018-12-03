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
# dylan_roof = textract.process("/Users/Carlo/Google Drive/FA18 Classes/SI508/Assignments - HW/Final Project/Manifesto-Project/Dylan_Roof.pdf", encoding='utf_8').decode()
# dylan_roof = dylan_roof.replace('\n', ' ')
# dylan_roof = dylan_roof.replace('6/20/2015lastrhodesian.com/data/documents/rtf88.txt', ' ')
# dylan_roof = dylan_roof.replace('http://lastrhodesian.com/data/documents/rtf88.txt2/4', ' ')
# dylan_roof = dylan_roof.replace('\u2026', '...')
# dylan_roof = dylan_roof.replace('\f', ' ')
# dylan_roof = dylan_roof.replace('\u2019', "'")
# dylan_roof = dylan_roof.replace('\u201c', '"')
# dylan_roof = dylan_roof.replace('\u201d', '"')
# dylan_roof = dylan_roof.replace('\u2013', ' - ')
#
# # print(dylan_roof)
# manifesto_dict = {}
# manifesto_dict['Dylan Roof'] = {}
# manifesto_dict['Dylan Roof']['Dylan Roof Manifesto'] = dylan_roof
# with open('manifesto-roof.json', 'a') as outfile:
#     json.dump(manifesto_dict, outfile)

# Elliot Rodger
# elliot_rodger = textract.process("/Users/Carlo/Google Drive/FA18 Classes/SI508/Assignments - HW/Final Project/Manifesto-Project/Elliot_Rodger.pdf", encoding='utf_8').decode()
# elliot_rodger = elliot_rodger.replace('\n', ' ')
# elliot_rodger = elliot_rodger.replace('\u2026', '...')
# elliot_rodger = elliot_rodger.replace('\f', ' ')
# elliot_rodger = elliot_rodger.replace('\u2019', "'")
# elliot_rodger = elliot_rodger.replace('\u201c', '"')
# elliot_rodger = elliot_rodger.replace('\u201d', '"')
# elliot_rodger = elliot_rodger.replace('\u2013', ' - ')
# manifesto_dict = {}
# manifesto_dict['Elliot Rodger'] = {}
# manifesto_dict['Elliot Rodger']['The Twisted World: The Story of Elliot Rodger'] = elliot_rodger
# with open('manifesto-rodger.json', 'a') as outfile:
#     json.dump(manifesto_dict, outfile)


# Seung Hui Cho
# seung_hui_cho = textract.process("/Users/Carlo/Google Drive/FA18 Classes/SI508/Assignments - HW/Final Project/Manifesto-Project/seung_hui_cho.pdf", encoding='utf_8').decode()
# seung_hui_cho = seung_hui_cho.replace('\n', ' ')
# seung_hui_cho = seung_hui_cho.replace('\u2026', '...')
# seung_hui_cho = seung_hui_cho.replace('\f', ' ')
# seung_hui_cho = seung_hui_cho.replace('\u2019', "'")
# seung_hui_cho = seung_hui_cho.replace('\u201c', '"')
# seung_hui_cho = seung_hui_cho.replace('\u201d', '"')
# seung_hui_cho = seung_hui_cho.replace('\u2013', ' - ')
# seung_hui_cho = seung_hui_cho.replace('\u2014', ' - ')
#
# manifesto_dict = {}
# manifesto_dict['Seung Hui Cho'] = {}
# manifesto_dict['Seung Hui Cho']['Seung Hui Cho Manifesto'] = seung_hui_cho
# with open('manifesto-cho.json', 'a') as outfile:
#     json.dump(manifesto_dict, outfile)


# Anders Breivik
# anders_breivik = textract.process("/Users/Carlo/Google Drive/FA18 Classes/SI508/Assignments - HW/Final Project/Manifesto-Project/Anders_Behring_Breivik.pdf", encoding='utf_8').decode()
# anders_breivik = anders_breivik.replace('\n', '')
# manifesto_dict = {}
# manifesto_dict['Anders Breivik'] = {}
# manifesto_dict['Anders Breivik']['2083: A European Declaration of Independence'] = anders_breivik
# with open('manifesto-anders.json', 'a') as outfile:
#     json.dump(manifesto_dict, outfile)

# Eric Auvinen
# eric_auvinen = textract.process("/Users/Carlo/Google Drive/FA18 Classes/SI508/Assignments - HW/Final Project/Manifesto-Project/Auvinen.doc", encoding='utf_8').decode()

# Ted Kaczynski
# ted_kaczynski = textract.process("/Users/Carlo/Google Drive/FA18 Classes/SI508/Assignments - HW/Final Project/Manifesto-Project/Ted_Kaczynski.pdf", encoding='utf_8')
# print(ted_kaczynski)

# Web Scraping
# CACHE_FNAME = "manifesto-cache.json"

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
# christopher_dorner = soup.find('blockquote').text
# christopher_dorner = christopher_dorner.replace('\n', ' ')
# manifesto_dict = {}
# manifesto_dict['Christopher Dorner'] = {}
# manifesto_dict['Christopher Dorner']["Christopher Dorner's Manifesto"] = christopher_dorner
# with open('manifesto-dorner.json', 'a') as outfile:
#     json.dump(manifesto_dict, outfile)
#     print("cached")


# print(manifesto_text)

# print(soup.find("a")) # For example
# page_title = soup.title.text
# print(page_title)
# manifesto_text = soup.find('div', class_ = 'entry-content')
# manifesto_text = manifesto_text.text
# manifesto_text = soup.find_all('td')



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
