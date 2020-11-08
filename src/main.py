import feedparser
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer

from parser import Parser


if __name__ == '__main__':
    parser = Parser()
    corpus = [parser.process(sentence) for sentence in parser.parse('news.rss', 'description')]

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus).toarray()

    # just output the input tokenized description and corresponding tfidf vectors
    for i, sentence in enumerate(corpus):
        print(sentence)
        print(list(X[i]))
