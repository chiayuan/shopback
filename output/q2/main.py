import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

from parser import Parser


if __name__ == '__main__':
    corpus = []
    with open('news.txt') as f:
        for line in f:
            corpus.append(line.rstrip())

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus).toarray()

    with open('output2.txt', 'w') as f:
        for i, sentence in enumerate(corpus):
            v = ','.join(map(str, X[i]))
            f.write(f'{sentence}\n')
            f.write(f'{v}\n')
