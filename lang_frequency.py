import sys
import re
from collections import defaultdict


def load_data(filepath):
    with open(filepath, 'r') as file:
        text = re.sub('\W+', ' ', file.read().lower())
    return text.split(' ')


def get_most_frequent_words(text):
    words = defaultdict(int)
    for word in text:
        words[word] += 1
    return sorted(words.items(), key=lambda word: word[1], reverse=True)[:10]


def pprint_frequent_words(sorted_words_list):
    print('Слова, которые встречаются в тексте чаще всего: \n')
    for word, counter in sorted_words_list:
        print('Слово: ', word, ' Количество повторений: ', counter, '\n')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('Вы не указали путь к файлу!')
    filepath = sys.argv[1]
    try:
        data = load_data(filepath)
    except FileNotFoundError:
        sys.exit('Файл отсутствует!')
    most_frequent_words = get_most_frequent_words(data)
    pprint_frequent_words(most_frequent_words)
