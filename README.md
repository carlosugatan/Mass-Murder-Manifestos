# Carlo Sugatan

## Mass-Murder-Manifestos
Text analysis of mass murderer manifestos

## Purpose
This project analyzed seven manifestos. This analysis was originally going to reference [Common Psycholinguistic Themes in Mass Murderer Manifestos](https://scholarworks.waldenu.edu/cgi/viewcontent.cgi?article=4596&context=dissertations) and [Knoll's psycholinguistic content](https://www.ncbi.nlm.nih.gov/pubmed/23107562). Overtime, a separate analysis was performed instead. Future work will delve deeper into the language analysis.

This program allows you to analyze the seven manifestos collected from the web using functions such as `word_cloud()` or `vulgar_words()`. See **Functions** part of this README.

## Note
Only seven manifestos were analyzed. I purposely left out Harris and Klebold (Columbine shooting) as their manifestos were written on different mediums across different pages of journals. I left out video manifestos as it would be difficult to transcribe them at this time. These are left for future work.


## Warning
**Analysis contain vulgar, offensive, and disturbing language.**

## Results
You can view the results **[here](https://github.com/carlosugatan/Mass-Murder-Manifestos/blob/master/Final%20Project%20Functions.ipynb)**

## How to run this program
- You don't have to run the program on your local machine! You can view the analysis [here!](https://github.com/carlosugatan/Mass-Murder-Manifestos/blob/master/Final%20Project%20Functions.ipynb)

- Download all the files on this repo. The `Manifesto Data` folder is not required. You don't have to run `data_scraper.py` nor `manifesto_func.py`
- Only run `class_manifesto.py`.
- In `class_manifesto.py`, the manifesto instances are already created. The commands to run the methods are written but commented out. These can be found on the bottom of the program. See **Functions** of this README for a detailed version of the methods and results you can expect.

## Necessary libraries
- You will need to install [Numpy](https://www.scipy.org/install.html), [WorldCloud](https://github.com/amueller/word_cloud), [Matplotlib](https://matplotlib.org/users/installing.html), [Pandas](https://pandas.pydata.org/getpandas.html), and [NLTK](https://www.nltk.org/install.html), to run this program.

- [Textract](https://textract.readthedocs.io/en/stable/) was used to scrape data from PDFs and Word documents. Not required unless you're interested in running `data_scraper.py` in which case, you would have to change the path of the file.

**Note on NLTK:**

You may have to install vader_lexicon through NLTK's installer.

`python` > `import nltk` > `nltk.download()` > `d` > `vader_lexicon`

See [here for details](https://stackoverflow.com/questions/43546593/error-message-with-nltk-sentiment-vader-in-python).

## Manifesto Data
The Manifesto JSON files are formatted as follows:
`manifesto_data[author][title]`
1. Jim Adkisson: The Adkisson Manifesto
2. Eric Auvinen: Natural Selector's Manifesto
3. Seung Hui Cho: Seung Hui Cho Manifesto
4. Christopher Dorner: Christopher Dorner's Manifesto
5. Ted Kaczynski: Industrial Society and Its Future
6. Elliot Rodger: The Twisted World: The Story of Elliot Rodger
7. Dylann Roof: Dylann Roof Manifesto

_PDFs of the manifestos are uploaded on `Data Manifesto` folder_

## Functions
- `word_cloud()` - Displays most used words in a word cloud visualization
- `vulgar_words()` - Displays most used vulgar words in a word cloud visualization
- `pronouns_analysis()` - Displays most used pronouns in a word cloud visualization. [Some studies about pronouns and personalities](https://hbr.org/2011/12/your-use-of-pronouns-reveals-your-personality).
- `sentiment_analysis()` - Displays polarity of text (positive, negative, neutral)

### Functions for all manifestos
- `word_count()` - Displays a graph to show the word count of all manifestos
- `unique_words()` - Displays a graph to show the unique words vs. word count of all manifestos

## Running the Unit Tests
Required file: `TESTS_Manifesto.py`

The top portion of the unit tests were written before OOP was implemented. This works for `manifesto_func.py`. **If you are running the tests, please also download `manifesto_func.py`.** Otherwise, the bottom portion are tests created to test the OOP implementation. This requires `class_manifesto.py`. All tests should pass. I wrote them specifically to pass because it was used to make sure data quality and cleaning was working properly.

## Project Requirements fulfilled
### Base Requirements
All base requirements were fulfilled. However, I only created one class instead of the required 2.

### Second Level Requirements
1. Scraping data using BeautifulSoup
2. Using a library in Python that we did not study in SI508 or used in any assignment
3. Object-orientation

### Third Level Requirements
1. Data visualization
2. Usable dataset (although only seven manifestos at the moment!)

## References
Some resources I used that helped me with this analysis.
1. [https://www.kaggle.com/ngyptr/python-nltk-sentiment-analysis](https://www.kaggle.com/ngyptr/python-nltk-sentiment-analysis)
2. [https://www.digitalvidya.com/blog/an-introduction-to-text-analysis-in-python/](https://www.digitalvidya.com/blog/an-introduction-to-text-analysis-in-python/)
3. [https://stackoverflow.com/questions/23591254/python-pandas-matplotlib-annotating-labels-above-bar-chart-columns](https://stackoverflow.com/questions/23591254/python-pandas-matplotlib-annotating-labels-above-bar-chart-columns)
4. [https://www.geeksforgeeks.org/removing-stop-words-nltk-python/](https://www.geeksforgeeks.org/removing-stop-words-nltk-python/)
5. [https://www.learndatasci.com/tutorials/sentiment-analysis-reddit-headlines-pythons-nltk/](https://www.learndatasci.com/tutorials/sentiment-analysis-reddit-headlines-pythons-nltk/)
6. [https://github.com/LearnDataSci/article-resources/blob/master/Sentiment%20Analysis%20on%20Reddit%20Headlines%20with%20NLTK/Sentiment%20Analysis%20on%20Reddit%20Headlines%20with%20NLTK.ipynb
](https://github.com/LearnDataSci/article-resources/blob/master/Sentiment%20Analysis%20on%20Reddit%20Headlines%20with%20NLTK/Sentiment%20Analysis%20on%20Reddit%20Headlines%20with%20NLTK.ipynb
)
7. [Common Psycholinguistic Themes in Mass Murderer Manifestos, Laura Hamlett](https://scholarworks.waldenu.edu/cgi/viewcontent.cgi?article=4596&context=dissertations)
