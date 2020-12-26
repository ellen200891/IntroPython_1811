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
import random
import json
import csv


def create_text_line(min_len, max_len):
    txt_list = [chr(random.randint(ord('a'), ord('z'))) for _ in range(random.randint(min_len, max_len))]
    return "".join(txt_list)


def create_number_line(min_len, max_len):
    txt_list = [chr(random.randint(ord('0'), ord('9'))) for _ in range(random.randint(min_len, max_len))]
    return "".join(txt_list)


def split_text_line(txt_line):
    space_count = len(txt_line) // 10
    space_index_list = []
    while len(space_index_list) < space_count:
        index = random.randint(1, len(txt_line) - 2)
        if (index not in space_index_list and
                index - 1 not in space_index_list and
                index + 1 not in space_index_list):
            space_index_list.append(index)
    for index in space_index_list:
        txt_line = txt_line[:index] + " " + txt_line[index + 1:]
    return txt_line


def replace_text_to_number(word):
    if len(word) > 5:
        return word
    else:
        return create_number_line(len(word), len(word))


def replace_first_letter(word):
    return word.replace(word[0], word[0].upper(), 1)


def replace_last_letter(word):
    signs = ',.;:!?'
    if len(word) < 4:
        return word
    else:
        return word[:-1] + random.choice(signs)


def create_randome_txt_data(min_len=100, max_len=1000):
    txt_line = create_text_line(min_len, max_len)
    txt_line = split_text_line(txt_line)
    new_words = []
    for word in txt_line.split():
        case = random.randint(1, 100)
        if not case % 10:
            new_word = replace_text_to_number(word)
        elif not case % 2:
            new_word = replace_first_letter(word)
        elif not case % 5:
            new_word = replace_last_letter(word)
        else:
            new_word = word
        new_words.append(new_word)
    return " ".join(new_words)


# Функция 2. Создает данные для записи в файл json.
# Создает и возвращает словарь со случайным количеством ключей (не менее 5 но не более 20 ключей).
# Ключи - уникальные случайные строки длинны 5 символов из маленьких букв английского алфавита
# (можно с повторениями символов).
# Значения - или целое число в диапазоне от -100 до 100, или число типа float в диапазоне от 0 до 1,
# или True/False. Выбор значения должен быть равновероятным. Т.е. вероятность того, что значение будет целым
# такая же, как и вероятность того, что будет типа float или типа bool.
def random_key_json_file():
    return "".join(chr(random.randint(ord("a"), ord("z"))) for _ in range(5))


def random_value_json_file():
    n = random.randrange(3)
    if n == 0:
        return random.randint(-100, 100)
    elif n == 1:
        return random.uniform(0, 1)
    else:
        return bool(random.randint(0, 1))


def create_randome_dict_json_file():
    new_dict = {}
    n = random.randint(5, 20)

    for _ in range(n):
        key = random_key_json_file()
        value = random_value_json_file()
        new_dict[key] = value
    return new_dict


# Функция 3. Создает данные для записи в файл csv.
# Создает и возвращает список длинны n внутренних списков длинны m (таблица с n строк и m столбцов).
# Числа n и m выбираются случайно в диапазоне от 3 до 10.
# В таблицу записывать значения только 0 или 1.
# Заголовка у таблицы нет.

def create_random_list_csv():
    m = random.randint(3, 10)
    n = random.randint(3, 10)
    new_list = [[random.randint(0, 1) for _ in range(m)] for _ in range(n)]
    return new_list


# А теперь основное задание:
# Написать функцию generate_and_write_file которая принимает один параметр - полный путь к файлу.
# В зависимости от расширения файла (txt, csv, json) сгенерировать данные для записи и записать в данный файл.
# Если расширение не соответствует заданным, то вывести текст "Unsupported file format"

def write_txt(filename):
    with open(filename, "w") as write_in_txt:
        write_txt = create_randome_txt_data()
        write_in_txt.write(write_txt)


def write_json(filename):
    with open(filename, "w") as write_in_json:
        json.dump(create_randome_dict_json_file(), write_in_json, indent=2)


def write_csv(filename):
    with open(filename, "w") as write_in_csv:
        writer = csv.writer(write_in_csv, delimiter=',')
        writer.writerow(create_random_list_csv())


def generate_and_write_file(filename):
    our_list = filename.split('.')[-1]
    if our_list == 'txt':
        result = write_txt(filename)
    elif our_list == "json":
        result = write_json(filename)
    elif our_list == "csv":
        result = write_csv(filename)
    else:
        print("Unsupported file format")
    return result


generate_and_write_file('test.csv')
