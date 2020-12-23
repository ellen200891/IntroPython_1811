# -*- coding: utf8 -*-
# # Цель задания - создать функции, которые будут генерировать случайные данные нужного формата
# # для записи в файлы разных типов.

# # Функция 1. Создает данные для записи в файл txt.
# # Функция генерирует и возвращает строку случайной длинны (не менее 100 но не более 1000 символов).
# # В строке должны присутствовать большие и маленькие буквы английского алфавита, цифры, пробелы,
# # знаки препинания, символ перехода на новую строку (\n).
# # Строка должна выглядеть как текст. Слова отделяться друг от друга пробелами.
# # Большие буквы только в начале слов. Цифры не должны быть частями слов, а стоять отдельно.
# # Знаки препинания всегда идут в конце слова.
import json
import csv
import random
import string

import random
import string

def randstring():
    return new_string
high_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
low_letters = 'abcdefghijklmnopqrstuvwxyz'
signs = '., \n'
number = '1234567890'
choice_string = (high_letters + low_letters + signs + number)
new_string = ''.join([random.choice(choice_string) for i in range(random.randint(100, 1000))])
print(new_string)
# Функция 2. Создает данные для записи в файл json.
# Создает и возвращает словарь со случайным количеством ключей (не менее 5 но не более 20 ключей).
# Ключи - уникальные случайные строки длинны 5 символов из маленьких букв английского алфавита
# (можно с повторениями символов).
# Значения - или целое число в диапазоне от -100 до 100, или число типа float в диапазоне от 0 до 1,
# или True/False. Выбор значения должен быть равновероятным. Т.е. вероятность того, что значение будет целым
# такая же, как и вероятность того, что будет типа float или типа bool.
#
# Функция 3. Создает данные для записи в файл csv.
# Создает и возвращает список длинны n внутренних списков длинны m (таблица с n строк и m столбцов).
# Числа n и m выбираются случайно в диапазоне от 3 до 10.
# В таблицу записывать значения только 0 или 1.
# Заголовка у таблицы нет.
#
# А теперь основное задание:
# Написать функцию generate_and_write_file которая принимает один параметр - полный путь к файлу.
# В зависимости от расширения файла (txt, csv, json) сгенерировать данные для записи и записать в данный файл.
# Если расширение не соответствует заданным, то вывести текст "Unsupported file format"