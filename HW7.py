# 1) Создать список из 20 случайных целых чисел в диапазоне от 1 до 100.
# Задание можно выполнить и через обычный цикл и через генератор списков.

import random

new_list = [random.randint(1, 100) for number in range(20)]
print(new_list)


###########################################################################
# 2) Создать словарь triangle в который записать точки A B C (ключи),
# и их координаты - кортежи (значения), созданные случайным образом с помощью модуля random в диапазоне от -10 до 10 по каждой оси.

triangle = {"A": (random.randint(-10, 10),
                  random.randint(-10, 10),
                  random.randint(-10, 10)),
            "B": (random.randint(-10, 10),
                  random.randint(-10, 10),
                  random.randint(-10, 10)),
            "C": (random.randint(-10, 10),
                  random.randint(-10, 10),
                  random.randint(-10, 10))}
print(triangle)
############################################################################

# 3) Создать функцию my_print, которая принимает в виде параметра строку и печатает ее
# с тремя символами * вначале и в конце строки.
# Пример:
# my_str = 'I'm the string'
# Печатает ***I'm the string***

def print_my_str(my_str):
    star = "***"
    print(f"{star}{my_str}{star}")

my_str = "I'm the string"
print_my_str(my_str)
###########################################################################
# 4) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена.
# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
# в) Посчитать среднее количество лет всех людей из списка.

persons = [{"name": "Luce", "age": 76}, {"name": "Nick", "age": 17}, {"name": "Alice", "age": 92}]
names_ages = [(person["name"], person["age"]) for person in persons]
min_age = persons[0]['age']
name_min_age = []
list_person = []
sum_start = 0
max_len_name = 0
max_name = []

for person in persons:
    list_person.append(person['age'])
    if person["age"] < min_age:
        min_age = person["age"]
    if len(person["name"]) > max_len_name:
        max_len_name = len(person["name"])

##############   A   ##############

for person in persons:
    if min_age == person['age']:
        name_min_age.append(person["name"])
name_min_age = ', '.join(name_min_age)
print(name_min_age)


##############  Б    ##############
for person in persons:
    if max_len_name == len(person['name']):
        max_name.append(person['name'])
max_name = ', '.join(max_name)
print(max_name)



##############  В    ##############
for number in list_person:
    people = len(list_person)
    sum_start+=number
    midl_age = sum_start // people
print(midl_age)

###########################################################################
# 5) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]}
my_dict_1 = {"street": "Lenina",
             "home": '5',
             "flat": "1"}
my_dict_2 = {"squer": '12',
             "flat": "2"}

##############  A   ##############
first_keys = set(my_dict_1.keys())
res_a = first_keys.copy()
second_keys = set(my_dict_2.keys())
second_keys2 = second_keys.copy()
res_a.update(second_keys2)
res_a = list(res_a)
print(res_a)
##############  Б   ##############

first_keys.difference_update(second_keys)
first_keys = list(first_keys)
print(first_keys)

##############  В    ##############

my_dict_3 = dict((key, my_dict_1[key]) for key in my_dict_1 if key not in my_dict_2)
print(my_dict_3)

##############  C    ##############
my_dict_4 = {}
keys_1 = set(my_dict_1.keys())
keys_2 = set(my_dict_2.keys())
for key in keys_1.union(keys_2):
    if key in my_dict_1 and key in my_dict_2:
        my_dict_4[key] = [my_dict_1[key], my_dict_2[key]]
    elif key in my_dict_1 and  key not in my_dict_2:
        my_dict_4[key] = my_dict_1[key]
    else:
        my_dict_4[key] = my_dict_2[key]
