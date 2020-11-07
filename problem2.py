import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

from parser import Parser


if __name__ == '__main__':
    parser = Parser()
    corpus = parser.parse('news.rss')

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus)
    word_map = {word: i for i, word in enumerate(vectorizer.get_feature_names())}
    X = X.toarray()
    np.savetxt('output2.txt', X)