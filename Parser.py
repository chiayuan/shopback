import jieba
import feedparser
from bs4 import BeautifulSoup


class Parser:
    
    def __int__(self):
        pass

    def _clean(self, html):
        soup = BeautifulSoup(html)
        text = soup.get_text().replace('\xa0', ' ')
        return list(jieba.cut(text))

    def parse(self, file_name):
        feeds = feedparser.parse(file_name).entries
        for feed in feeds:
            print('title', feed.get('title', ''))
            print('description', self._clean(feed.get('description', '')))
            print('===')


if __name__ == '__main__':
    parser = Parser()
    parser.parse('news.rss')