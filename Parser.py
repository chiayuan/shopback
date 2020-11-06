import jieba
import feedparser
from typing import List, Any
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

class Parser:
    
    def __int__(self) -> None:
        pass

    def _tokenize(self, s: str) -> List[str]:
        """Given a string, return a list of tokens that tokenized by jieba"""
        tokens = jieba.cut(s)
        return [token.strip() for token in tokens if token.strip()]

    def _clean(self, html: Any) -> str:
        """Given html string, remove tags and control sysmbols, and return the tokenized sentence"""
        soup = BeautifulSoup(html)
        text = soup.get_text().replace('\xa0', ' ')
        return ' '.join(self._tokenize(text))

    def parse(self, file_name: str) -> List[str]:
        """Given a rss file, return tokenized description (split by space)"""
        feeds = feedparser.parse(file_name).entries
        return [self._clean(feed.get('description', '')) for feed in feeds]


if __name__ == '__main__':
    parser = Parser()
    corpus = parser.parse('news.rss')

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus)
    word_map = {word: i for i, word in enumerate(vectorizer.get_feature_names())}
    X = X.toarray()

    for i, s in enumerate(corpus):
        l = []
        for w in s.split():
            j = word_map.setdefault(w.lower(), -1)

            if j == -1:
                l.append((w.lower(), 0.0))
            else:
                l.append((w.lower(), X[i][j]))
        print(s)
        print(l)
        print("===")
