from parser import Parser


if __name__ == '__main__':
    parser = Parser()
    corpus = parser.parse('news.rss')

    with open('output.txt', 'w') as f:
        for sentence in corpus:
            f.write(f'{sentence}\n')
