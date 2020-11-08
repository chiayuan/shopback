### Introduction
Given a list of tokenized article,
transform them into tf-idf vectors.
Further applications probably be documents clustering or getting the most similar articles by given one.

In this question, I use scikit-learn (https://scikit-learn.org/stable/).
scikit-learn is known as machine learning toolkits,
and tf-idf is a very common algorithm in data mining, natural language processing.
So without any doubts, we can find tf-idf implementation in scikit-learn.
Moreover, the question asks us to transform each news article to a vectors, 
scikit-learn provides TfidfVectorizer to process the given corpus to a tf-idf matrix.


### Run
It is the same as question 1, so I just copy/paste the same description:

This program is build upon python 3.9 and pyenv/pipenv.
If you have pyenv, pipenv and python 3.9 in your environment,
got back to the root path of the project and run "pipenv --python 3.9.0", "pipenv install"

If not, I have provided the requirement file in the root path
run "pip install -r requirements.txt".

After that, change directory to question 1, 
use "pipenv run python main.py" or "python main.py" to get the result