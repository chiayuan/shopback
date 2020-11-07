import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

from parser import Parser


if __name__ == '__main__':
    corpus = []
    with open('output1.txt') as f:
        for line in f:
            corpus.append(line.rstrip())

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus)
    np.savetxt('output2.txt', X.toarray())
