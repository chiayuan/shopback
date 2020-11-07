import re
from typing import List, Any

import jieba
import feedparser
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer

class Parser:
    
    def __int__(self):
        pass

    def _tokenize(self, s: str) -> List[str]:
        """Given a string, return a list of tokens that tokenized by jieba"""
        tokens = jieba.cut(s)
        return [token.strip() for token in tokens if token.strip()]

    def _clean(self, html: Any) -> str:
        """Given html string, remove tags and control sysmbols, and return the tokenized sentence"""
        # remove tags
        soup = BeautifulSoup(html)
        text = soup.get_text().replace('\xa0', ' ')

        # use regex to remove meaningless chars
        regex = r'[a-zA-Z\u4e00-\u9fff]+'
        text = ' '.join(re.findall(regex, text))
        
        # to lowercase
        text = text.lower()

        return ' '.join(self._tokenize(text))
    def parse(self, file_name: str) -> List[str]:
        """Given a rss file, return tokenized description (split by space)"""
        feeds = feedparser.parse(file_name).entries
        return [self._clean(feed.get('description', '')) for feed in feeds]


if __name__ == '__main__':
    # part 1
    parser = Parser()
    corpus = parser.parse('news.rss')

    # part 2
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus)
    word_map = {word: i for i, word in enumerate(vectorizer.get_feature_names())}
    X = X.toarray()
