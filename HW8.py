# 1. Считать данные из файла domains.txt
# Названия интернет доменов сохранить их в виде списка строк (названия сохранить без точки).
import os

with open("C:/Users/Пользователь/Desktop/Hillel1/IntroPython_1811/domains.txt", 'rt', encoding="utf-8") as txt_file:
    domains = []
    for line in txt_file.readlines():
        line = line.replace('.', '')
        domains.append(line.strip())
print(domains)

###########################################################################################
# 2. Считать данные из файла names.txt и сохранить в список только фамилии из файла.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
# Фамилия находится всегда на одной и той же позиции в строке.

with open("names.txt", 'r') as txt_file:
    names = []
    for line in txt_file.readlines():
        line = line.replace('.', '')
        names.append(line.split('\t')[1])
print(names)

###########################################################################################
# 3. Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать из списков, полученных в задачах 1 и 2 и переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
# Буквы в строке МОГУТ повторяться (перемешивание алфавита не подойдет, так как буквы не смогут повторяться)

# Пример вызова функции:
# e_mail = create_email(domains, names)
# print(e_mail)
import random


def create_number():
    new_number = random.randint(100, 999)
    return new_number

def create_letter():
    alph = [chr(number) for number in range(ord('a'), ord('z') + 1)]
    alph = ''.join([random.choice(alph) for element in range(random.randint(5, 7))])
    return alph

def create_email(names,domains):
    names = random.choice(names)
    domains = random.choice(domains)
    number = create_number()
    string = create_letter()
    result = (f"{names}.{number}@{string}.{domains}")
    return result

print(create_email(names,domains))



# e_mail = create_email()
# шафл или   рендом чойс для доменов и имен
# >>>miller.249@sgdyyur.com
