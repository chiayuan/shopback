import re
from typing import List, Any

import jieba
import feedparser
from bs4 import BeautifulSoup


class Parser:
    
    def __init__(self):
        pass

    def _tokenize(self, s: str) -> List[str]:
        """Given a string, return a list of tokens that tokenized by jieba"""
        tokens = jieba.cut(s)
        return [token.strip() for token in tokens if token.strip()]

    def _clean(self, html: Any) -> str:
        """Given html string, remove tags and control sysmbols and return."""
        # remove tags
        soup = BeautifulSoup(html, 'html.parser')
        text = soup.get_text().replace('\xa0', ' ')

        # use regex to remove meaningless chars
        regex = r'[a-zA-Z\u4e00-\u9fff]+'
        text = ' '.join(re.findall(regex, text))
        
        # to lowercase
        text = text.lower()
        return text

    def parse(self, file_name: str, field: str) -> List[str]:
        """Given a rss file and field name, return a list of corresponding field content"""
        feeds = feedparser.parse(file_name).entries
        return [feed.get(field, '') for feed in feeds]

    def process(self, raw_text: str) -> str:
        """Given a raw html string, return the cleaned and tokenized version of it"""
        text = self._clean(raw_text)
        text = ' '.join(self._tokenize(text))
        return text
