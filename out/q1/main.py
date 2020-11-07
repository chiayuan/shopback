from parser import Parser


if __name__ == '__main__':
    parser = Parser()
    corpus = parser.parse('news.rss')

    with open('output.txt', 'w') as f, open('../q2/news.txt', 'w') as f_etl:
        for sentence in corpus:
            f.write(f'{sentence}\n')
            f_etl.write(f'{sentence}\n')
