# -*- coding: utf8 -*-
import requests
import json
import re


# 1. Написать функцию, которая принимает в виде параметра целое число - количество цитат (см. урок 12).
# Надо получить ровно столько не повторяющихся цитат с данными и сохранить их в csv файл
# (имя файла сделать параметром по умолчанию).
# Заголовки файла:
# Author, Quote, URL. Если автор не указан, цитату не брать.
# Перед сохранением в csv, записи отсортировать по автору (в алфавитном порядке).


# url = "http://api.forismatic.com/api/1.0/"
#
# params = {"method": "getQuote",
#           "format": "json",
#           "key": 1,
#           "lang": "ru"}
# for i in range(10):
#     params["key"] = i
#     r = requests.get(url, params=params)
#     quote = r.json()
#     # print(quote)
#     quote_text = quote["quoteText"]
#     print(quote_text)
#     quote_author = quote["quoteAuthor"]
#     print(quote_author)


###################################################################################################################
# 2. Дан файл authors.txt
# 2.1) написать функцию, которая считывает данные из этого файла,
# возвращая СПИСОК тех строк в которых есть полная дата, писатель и указание на его день рождения или смерти.
# Например: 26th February 1802 - Victor Hugo's birthday - author of Les Misérables.
def read_txt(filename="authors.txt"):
    with open(filename, 'r') as file:
        data = []
        for line in file.readlines():
            if line.find("birthday") >= 0 or line.find("death") >= 0:
                data.append(line)
    return data


list_autors = read_txt()


###################################################################################################################

# 2.2) Написать функцию, которая принимает список строк полученной в пункте 2.1, и возвращает список словарей
# в формате {"name": name, "date": date},
# где name это имя автора, а date - дата из строки в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
# Например [{"name": "Charles Dickens", "date": "09/06/1870"}, ...,
# {"name": "J. D. Salinger", "date": "01/01/1919"}]
def list_to_dict(list_autors):
    for autor in list_autors:
        name = dict_names(autor)
        date = [dict_data(autor)]
        keys = ['name', 'date']
        zipped = zip(name, date)
        dicts_names_data = [dict(zip(keys, values)) for values in zipped]
        print(dicts_names_data)
    # return dicts_names_data


# print(dicts_names_data)


def dict_names(autor):
    old_dict_names = re.findall(r"[a-zA-Z. ]+[']", autor)
    dict_names = [i.strip(' \'') for i in old_dict_names]
    return dict_names


month_name_map = {
    'January': "01",
    'February': "02",
    'March': "03",
    'April': "04",
    'May': "05",
    'June': "06",
    'July': "07",
    'August': "08",
    'September': "09",
    'October': "10",
    'November': "11",
    'December': "12"
}


def dict_data(autor):
    old_dict_data = re.findall(r"[0-9]\S+ \S+ \S+[0-9]", autor)
    data_list = []
    year = re.findall(r"[0-9]+", autor)[-1]
    day = re.findall(r"[0-9]+", autor)[0]
    month = re.findall(r"[A-Z][a-z]+[ ][1]", autor)
    month_names = ''.join([i.strip(' 1') for i in month])
    month_names = month_name_map[month_names]
    result = (f"{day}/{month_names}/{year}")
    return result


list_to_dict(list_autors)

# names = list_to_dict(name)
# dates = data
# def dict_names_data():
#     keys = ['name', 'data']
#     zipped = zip(name, data)
#     dicts_names_data = [dict(zip(keys, values)) for values in zipped]
#     return dicts_names_data
#
# print(dict_names_data())

##################################################################################################################
# 2.3) Написать функцию, которая сохраняет результат пункта 2.2 в json файл.
