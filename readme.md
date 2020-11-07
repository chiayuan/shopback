## Shopback Interview Take-home Test
- interviewee: Chia-Yuan Liu
- email: chiayuanliu.tw@gmail.com


## Prerequisites
### For question 1
- [feedparser](https://github.com/kurtmckee/feedparser): general usage for parsing rss format xml
- [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/): furthur data cleaning for text with html tags
- [jieba](https://github.com/fxsjy/jieba): chinese tokenizer

### For question 2
- [scikit-learn](https://scikit-learn.org/stable/): tf-idf vector generation


## Environment
This project is built on `Python 3.9`,  
and using `pyenv` and `pipenv` to isolate the environment from my workspace  
Please use these two tool to get the best experience to review my work.  
If not, there is also a `requirements` file for `pip install`.

Please follow instructions below to setup the environment:

### Without pyenv and pipenv
- Install all the packages
```bash
pip install -r requirements.txt
```

### Using pyenv and pipenv
- Install Python 3.9.0 using pyenv
```bash
pyenv install 3.9.0
```
- Build a virtualenv base on Pipfile
```bash
pipenv install
```

## Run
The followings run with pipenv.  
If you don't have isolated environment, just run with `python main.py`
### question 1
```bash
cd ${PROJECT_PATH}/output/q1
pipenv run python main.py
```

### question 2
```bash
cd ${PROJECT_PATH}/output/q2
pipenv run python main.py
```

## Reference
- [Regular Expression Cheatsheet](https://blog.typeart.cc/正則表達式-全型英數中文字、常用符號unicode對照表/)
- [How to get the latest COVID-19 News using Google News Feed - towardsdatascience](https://towardsdatascience.com/how-to-get-the-latest-covid-19-news-using-google-news-feed-950d9deb18f1)