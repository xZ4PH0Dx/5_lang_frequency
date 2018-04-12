import sys
import re
from collections import Counter


def load_file(filepath):
    with open(filepath, 'r') as file:
        return file.read()


def get_words_list(loaded_file):
    words_list = re.sub('\W+', ' ', loaded_file.lower())
    return words_list.split(' ')


def get_most_frequent_words(words_list):
    number_of_words = 10
    words = Counter(words_list)
    return words.most_common(number_of_words)


def pprint_frequent_words(sorted_words_list):
    print('Слова, которые встречаются в тексте чаще всего: \n')
    for word, counter in sorted_words_list:
        print('{:>12} {:>6}\n'.format(word, counter))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('Вы не указали путь к файлу!')
    filepath = sys.argv[1]
    try:
        loaded_text = load_file(filepath)
    except FileNotFoundError:
        sys.exit('Файл отсутствует!')
    words_list = get_words_list(loaded_text)
    most_frequent_words = get_most_frequent_words(words_list)
    pprint_frequent_words(most_frequent_words)
