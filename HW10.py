# -*- coding: utf8 -*-

import json
import re

#### 1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла. ###########
def open_json_data():
    with open("data.json", "r") as json_file:
        new_data = json.load(json_file)
        return new_data

dict_list = open_json_data()

# 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
def key_sorted_by_surname(obj_dict):
    surname = re.findall(r'[A-Z]', obj_dict["name"])
    surn = surname[-1]
    return surn

new_dict_list = sorted(dict_list, key=key_sorted_by_surname)
print(new_dict_list)

#### 3. Написать функцию сортировки по дате смерти из поля "years". ###########

def key_sorted_by_data(obj_dict):
    years = re.findall(r'[0-9]+', obj_dict["years"])
    d_data = years[-1]
    d_data = -int(d_data) if "BC" in obj_dict["years"] else int(d_data)
    return int(d_data)

new_dict_list = sorted(dict_list, key=key_sorted_by_data)
print(new_dict_list)

#### 4. Написать функцию сортировки по количеству слов в поле "text". ###########

def key_sorted_by_count_word(obj_dict):
    list = re.findall(r" ", obj_dict["text"])
    return len(list)

new_dict_list = sorted(dict_list, key=key_sorted_by_count_word)
print(new_dict_list)
