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

# Eric Auvinen
# eric_auvinen = textract.process("/Users/Carlo/Google Drive/FA18 Classes/SI508/Assignments - HW/Final Project/Manifesto-Project/Auvinen.doc", encoding='utf_8').decode()
# eric_auvinen = eric_auvinen.replace('\n', ' ')
# eric_auvinen = eric_auvinen.replace('\u2019', "'")
# eric_auvinen = eric_auvinen.replace('\u201c', "'")
# eric_auvinen = eric_auvinen.replace('\u201d', "'")
# manifesto_dict = {}
# manifesto_dict['Eric Auvinen'] = {}
# manifesto_dict['Eric Auvinen']["Natural Selector's Manifesto"] = eric_auvinen
# with open('manifesto-auvinen.json', 'a') as outfile:
#     json.dump(manifesto_dict, outfile)

# Ted Kaczynski
# ted_kaczynski = textract.process("/Users/Carlo/Google Drive/FA18 Classes/SI508/Assignments - HW/Final Project/Manifesto-Project/Ted_Kaczynski.pdf", encoding='utf_8').decode()
# ted_kaczynski = ted_kaczynski.replace('\n', ' ')
# ted_kaczynski = ted_kaczynski.replace('\f', ' ')
# ted_kaczynski = ted_kaczynski.replace('\u2019', "'")
# ted_kaczynski = ted_kaczynski.replace('\u201c', "'")
# ted_kaczynski = ted_kaczynski.replace('\u201d', "'")
# ted_kaczynski = ted_kaczynski.replace('\u2014', ' - ')
# manifesto_dict = {}
# manifesto_dict['Ted Kaczynski'] = {}
# manifesto_dict['Ted Kaczynski']["Industrial Society and Its Future"] = ted_kaczynski
# with open('manifesto-kaczynski.json', 'a') as outfile:
#     json.dump(manifesto_dict, outfile)

## TODO: Scrape data
# Anders Breivik
# anders_breivik = textract.process("/Users/Carlo/Google Drive/FA18 Classes/SI508/Assignments - HW/Final Project/Manifesto-Project/Anders_Behring_Breivik.pdf", encoding='utf_8').decode()
# anders_breivik = anders_breivik.replace('\n', '')
# manifesto_dict = {}
# manifesto_dict['Anders Breivik'] = {}
# manifesto_dict['Anders Breivik']['2083: A European Declaration of Independence'] = anders_breivik
# with open('manifesto-anders.json', 'a') as outfile:
#     json.dump(manifesto_dict, outfile)


# Christopher Dorner
# url_to_scrape = "http://www.laist.com/2013/02/07/christopher_dorners_manifesto_in_fu.php"
# manifesto_text = soup.find('blockquote').text
# christopher_dorner = soup.find('blockquote').text
# christopher_dorner = christopher_dorner.replace('\n', ' ')
# christopher_dorner = christopher_dorner.replace('\u2026', '...')
# christopher_dorner = christopher_dorner.replace('\f', ' ')
# christopher_dorner = christopher_dorner.replace('\u2019', "'")
# christopher_dorner = christopher_dorner.replace('\u201c', "'")
# christopher_dorner = christopher_dorner.replace('\u201d', "'")
# christopher_dorner = christopher_dorner.replace('\u2013', ' - ')
# christopher_dorner = christopher_dorner.replace('\u2014', ' - ')
# manifesto_dict = {}
# manifesto_dict['Christopher Dorner'] = {}
# manifesto_dict['Christopher Dorner']["Christopher Dorner's Manifesto"] = christopher_dorner

# Adkission Manifesto
# url_to_scrape = "https://faith17983.wordpress.com/2015/05/31/the-adkisson-manifesto/"
# manifesto_text = soup.find('div', class_ = 'entry-content')
# manifesto_text = manifesto_text.text
# jim_adkission = soup.find('div', class_ = 'entry-content')
# jim_adkission = jim_adkission.text
# jim_adkission = jim_adkission.replace('\n', ' ')
# jim_adkission = jim_adkission.replace('\u201c', "'")
# jim_adkission = jim_adkission.replace('\u201d', "'")
# jim_adkission = jim_adkission.replace('\u2019', "'")
# manifesto_dict = {}
# manifesto_dict['Adkission Manifesto'] = {}
# manifesto_dict['Adkission Manifesto']["The Adkission Manifesto"] = jim_adkission


# Web Scraping
# CACHE_FNAME = "manifesto-cache.json"

# primary_cache = Cache(CACHE_FNAME)
#
# while primary_cache.get(url_to_scrape) is None:
# 	data = requests.get(url_to_scrape)
# 	html_text = data.text
# 	primary_cache.set(url_to_scrape,html_text)
#
# soup = BeautifulSoup(primary_cache.get(url_to_scrape), features="html.parser")

# with open('manifesto-adkission.json', 'a') as outfile:
#     json.dump(manifesto_dict, outfile)
#     print("cached")


# print(manifesto_text)

# print(soup.find("a")) # For example
# page_title = soup.title.text
# print(page_title)
# manifesto_text = soup.find('div', class_ = 'entry-content')
# manifesto_text = manifesto_text.text
# manifesto_text = soup.find_all('td')


# Web Scraping Vulgar Words
url_to_scrape = "https://www.noswearing.com/dictionary/a"
CACHE_FNAME = "vulgar_words.json"

primary_cache = Cache(CACHE_FNAME)

while primary_cache.get(url_to_scrape) is None:
	data = requests.get(url_to_scrape)
	html_text = data.text
	primary_cache.set(url_to_scrape,html_text)

soup = BeautifulSoup(primary_cache.get(url_to_scrape), features="html.parser")

# with open('manifesto-adkission.json', 'a') as outfile:
#     json.dump(manifesto_dict, outfile)
#     print("cached")

page_title = soup.title.text
print(page_title)
