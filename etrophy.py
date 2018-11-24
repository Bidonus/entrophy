import codecs  # Для чтения кириллического текста
import re  # Для поиска слов в файле по регулярному вырожению
from collections import Counter  # Для расчёта частот
from itertools import islice  # Для итерации входного текста
from math import log2  # Для вычисления логарифма
import csv


def calculate_bigrams_and_letters() -> tuple:
    """
    Расчёт частоты букв и биграмм в тексте
    file_path - пусть к текстовому файлу
    Возвращает словари <буква/биграмма>:<частота>
    """

    file_path = './text.txt'
    with codecs.open(file_path, 'r', encoding='utf8') as file:
        letters = Counter()
        bigrams = Counter()
        for letter in file:
            letters += Counter(letter.strip())
            words = re.findall("\w+", letter)
            bigrams += Counter(zip(words, islice(words, 1, None)))
        return dict(letters), dict(bigrams)


def calculate_entrophy():
    """
    Расчёт энтропии
    p1 - частоты букв
    p2 - частоты биграмм
    Возвращает h1, h2 - энтропия для частот букв, частот биграмм
    """
    p1, p2 = calculate_bigrams_and_letters()
    h1 = 0
    h2 = 0

    for entr1 in p1.values():
        h1 -= entr1 * log2(entr1)
    for entr2 in p2.values():
        h2 -= entr2 * log2(entr2)

    return h1, h2


def save_to_file():
    """
    Сохранения результатов в результирующий файл result.csv
    """
    p1, p2 = calculate_bigrams_and_letters()
    h1, h2 = calculate_entrophy()
    data = {'Letters': p1,
            'Bigrams': p2,
            'Entrophy for letters': h1,
            'Entrophy for bigrams': h2,
            }
    with open('result.csv', 'w') as f:
        writer = csv.writer(f, delimiter=':')
        for i in data.items():
            writer.writerow(i)


if __name__ == '__main__':
    save_to_file()
