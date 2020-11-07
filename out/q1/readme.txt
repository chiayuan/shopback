### Introduction
This question is about scraping through an rss feed url,  
cleaning and parsing data into required format.

Therefore, I used python and the following libraries:
- feedparser: https://github.com/kurtmckee/feedparser
- beautifulsoup: https://www.crummy.com/software/BeautifulSoup/
- jieba: https://github.com/fxsjy/jieba

Although we can use beautifulsoup to deal with such xml/html alike file.
With limited deadline, I would like to save efforts on text processing more than scraping.
By feedparser, it structurize the xml into a way easier to read (dictionary based).
After get feeds and it's structurized dictionary format, extract the description field,
then using beautifulsoup to extract words from dirty string with a lot of html tags.

Finally, I use regular expression to filter symbols and numbers to get meaningful words
, and tokenize the string by jieba.

### Run
This program is build upon python 3.9 and pyenv/pipenv.
If you have pyenv, pipenv and python 3.9 in your environment,
got back to the root path of the project and run "pipenv install"

If not, I have provided the requirement file in the root path
run "pip install -r requirements.txt".

After that, change directory to question 1, 
use "pipenv run python main.py" or "python main.py" to get the result