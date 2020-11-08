from parser import Parser


if __name__ == '__main__':
    parser = Parser()
    corpus = parser.parse('news.rss', 'description')

    with open('description.txt', 'w') as f_des, open('output.txt', 'w') as f, open('../q2/news.txt', 'w') as f_etl:
        for sentence in corpus:
            tokens = parser.process(sentence)
            f_des.write(f'{sentence}\n')
            f.write(f'{tokens}\n')
            f_etl.write(f'{tokens}\n')
